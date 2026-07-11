# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



