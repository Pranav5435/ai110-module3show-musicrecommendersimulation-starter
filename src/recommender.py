import csv
from typing import List, Dict, Tuple, Any
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = _profile_to_prefs(user)
        scored_songs = []
        for song in self.songs:
            score, _reasons = score_song(user_prefs, song)
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = _profile_to_prefs(user)
        _, reasons = score_song(user_prefs, song)
        return "; ".join(reasons) if reasons else "No specific reasons available."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    genre_target = _get_value(user_prefs, "genre")
    song_genre = _get_value(song, "genre")
    if genre_target and song_genre and _normalize_text(genre_target) == _normalize_text(song_genre):
        score += 4.0
        reasons.append("genre match (+4.0)")

    mood_target = _get_value(user_prefs, "mood")
    song_mood = _get_value(song, "mood")
    if mood_target and song_mood and _normalize_text(mood_target) == _normalize_text(song_mood):
        score += 2.0
        reasons.append("mood match (+2.0)")

    for feature_name, weight in (
        ("energy", 1.0),
        ("balance", 1.0),
        ("danceability", 1.0),
        ("acousticness", 1.0),
    ):
        target_value = _get_value(user_prefs, feature_name)
        song_value = _resolve_numeric_value(song, feature_name)
        if target_value is None or song_value is None:
            continue

        closeness = _closeness_score(float(target_value), float(song_value))
        feature_score = closeness * weight
        score += feature_score
        if feature_score > 0:
            reasons.append(f"{feature_name} close to target (+{feature_score:.1f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]


def _normalize_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip().lower()


def _get_value(source: Any, key: str) -> Any:
    if isinstance(source, dict):
        return source.get(key)
    if hasattr(source, key):
        return getattr(source, key)
    if hasattr(source, "__dict__"):
        return source.__dict__.get(key)
    return None


def _resolve_numeric_value(song: Any, feature_name: str) -> Any:
    value = _get_value(song, feature_name)
    if value is not None:
        return value

    if feature_name == "balance":
        return _get_value(song, "valence")
    return None


def _closeness_score(target: float, value: float) -> float:
    distance = abs(target - value)
    closeness = 1.0 - distance
    return max(0.0, min(1.0, closeness))


def _profile_to_prefs(user: UserProfile) -> Dict[str, Any]:
    return {
        "genre": user.favorite_genre,
        "mood": user.favorite_mood,
        "energy": user.target_energy,
        "balance": 0.7,
        "danceability": 0.7,
        "acousticness": 0.0 if not user.likes_acoustic else 0.7,
    }
