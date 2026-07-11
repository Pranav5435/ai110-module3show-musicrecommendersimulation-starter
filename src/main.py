"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:  # pragma: no cover - supports running as a script
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Example profile tuned toward an energetic, bass-forward house vibe
    user_prefs = {"genre": "house", "mood": "energetic", "energy": 0.9, "balance": 0.8, "danceability": 0.9, "acousticness": 0.1}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
