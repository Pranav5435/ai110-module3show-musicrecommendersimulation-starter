# 🎵 Music Recommender Simulation

## Project Summary
This project simulates a basic content-based music recommender. It takes a user's taste profile, genre, mood, energy, emotional balance, danceability, and acousticness, and scores every song in a catalog based on how closely it matches those preferences. Genre and mood are weighted the heaviest, acting as strong signals of fit, while the remaining features are scored by closeness rather than exact match. The system then ranks the full catalog and returns the top matches, giving a clear, explained recommendation for why each song was selected.
---

## How The System Works
This recommender takes a user's music taste and a catalog of songs, then orders the songs by how well they match what the user would actually want to listen to. Real platforms like Spotify or YouTube do something similar at a much larger scale, often blending content-based filtering (matching a user's preferences to a song's attributes) with collaborative filtering (using patterns from other users' behavior). This version focuses only on content-based filtering. It scores every song based on how closely it matches the user's preferred genre, mood, energy, emotional balance, danceability, and acousticness, then ranks the full list from highest to lowest score to produce the top recommendations.

Finalized algorithm recipe:
- Genre match: +4.0 points
- Mood match: +2.0 points
- Energy closeness: up to +1.0 points
- Balance closeness: up to +1.0 points
- Danceability closeness: up to +1.0 points
- Acousticness closeness: up to +1.0 points
- Maximum possible score: 10.0

Since genre and mood carry the most weight, the system may under-value songs that are a strong overall vibe match but fall in a different genre category, potentially creating a filter bubble around the user's stated genre.

Song and UserProfile features:

- genre
- mood
- energy
- balance
- danceability
- acousticness
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Top recommendations:
1. City of Sparks
   Final score: 9.89
   Reasons:
     - genre match (+4.0)
     - mood match (+2.0)
     - energy close to target (+1.0)
     - balance close to target (+1.0)
     - danceability close to target (+1.0)
     - acousticness close to target (+0.9)
2. Gym Hero
   Final score: 3.87
   Reasons:
     - energy close to target (+1.0)
     - balance close to target (+1.0)
     - danceability close to target (+1.0)
     - acousticness close to target (+0.9)
3. Golden Hour Drive
   Final score: 3.79
   Reasons:
     - energy close to target (+1.0)
     - balance close to target (+0.9)
     - danceability close to target (+0.9)
     - acousticness close to target (+1.0)
4. Neon Alley
   Final score: 3.75
   Reasons:
     - energy close to target (+0.9)
     - balance close to target (+0.9)
     - danceability close to target (+0.9)
     - acousticness close to target (+1.0)
5. Sunrise City
   Final score: 3.69
   Reasons:
     - energy close to target (+0.9)
     - balance close to target (+1.0)
     - danceability close to target (+0.9)
     - acousticness close to target (+0.9)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried
I tested six distinct user profiles: house/electronic, chill/lo-fi, deep/intense rock, plus three adversarial edge cases (a conflicted energy profile with contradictory preferences, a genre-trap profile, and an extreme-boundary profile). Across all profiles, a clear pattern emerged: whichever song matched the user's stated genre and mood jumped far ahead of the rest, while every other song clustered together in a much lower score range based only on closeness scoring. The lo-fi profile stood out as an exception, since multiple songs scored highly (above 7.0), showing that the closeness-based features can meaningfully separate songs even without a genre match, when there's enough dataset coverage for that genre. Full results and analysis are documented in model_card.md.
---

## Limitations and Risks
One clear limitation is that genre and mood create a scoring "cliff" instead of a smooth ranking. Since a genre match alone can be worth up to 4.0 out of 10 points, any song that hits the user's stated genre jumps way ahead of everything else, even if some of those other songs are nearly perfect matches on energy, mood, and vibe. This means the system struggles to meaningfully differentiate between non-matching songs, since their scores cluster tightly together regardless of how close or far their actual vibe is. In practice, this could create a filter bubble, where users only ever see their exact stated genre reinforced. The dataset itself is also limited to 18 songs across a handful of genres, so results may not generalize well to tastes outside what's represented (see model_card.md for a full breakdown of missing genres).
---

## Reflection
Building this recommender showed me how directly a scoring system's weights shape its behavior, watching one song score 9.89 while everything else clustered in the high 3s made the abstract idea of "genre bias" into something concrete I could see in my own terminal. It also clarified how recommenders turn raw data into predictions: it's not magic, it's just a defined set of rules applied consistently across a dataset. Where this gets ethically interesting is realizing that even a simple, transparent scoring system like mine can create a filter bubble, and real platforms with much more complex and opaque logic likely have similar effects at a much larger scale. Full reflection is available in model_card.md.


