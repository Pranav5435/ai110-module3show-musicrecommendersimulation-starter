# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 
Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
One clear limitation is that genre and mood create a scoring "cliff" instead of a smooth ranking. Since a genre match alone can be worth up to 4.0 out of 10 points, any song that hits the user's stated genre jumps way ahead of everything else, even if some of those other songs are nearly perfect matches on energy, mood, and vibe. Because of this, the scores for non-matching songs end up clustered close together (usually within a point or two of each other), which makes it hard for the system to tell a "pretty good fit" from a "just okay" one once genre is off the table. In practice, this could create a filter bubble: the system will keep recommending the same genre over and over, even when a different genre might actually match what the user's looking for mood and energy wise. This is a direct tradeoff of the decision to make genre and mood dominate the scoring, so it's expected behavior, but it's still a real weakness worth noting.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  
I tested six different profiles to see how the recommender reacts to different tastes, plus a couple of edge cases meant to try to break it, starting with house/electronic versus chill/lo-fi, which landed on completely different top picks, exactly what I wanted to see, since the house profile pulled "City of Sparks" way out in front at 9.89, while the lo-fi profile favored "Library Rain" and "Midnight Coding," both scoring above 9.0, and what's interesting is that the lo-fi profile's top 3 all stayed above 7.0, while the house profile's results dropped off a cliff after song 1, which tells me lo-fi as a genre/mood combo happens to be better represented in my dataset, so there were more strong matches to go around; then comparing deep/intense rock to house/electronic, both profiles had one dominant winner ("Storm Runner" at 9.40 for rock, "City of Sparks" at 9.89 for house), then a steep drop to songs in the 3.0 to 4.8 range, which confirmed that the scoring cliff I noticed isn't unique to one profile, it's a pattern baked into how genre and mood dominate the math, regardless of which genre you're asking for; the conflicted energy profile, an edge case designed to have contradictory preferences, showed this clearly too, since the top two results ("Sunrise City" at 7.35 and "Gym Hero" at 7.33) were nearly tied, which makes sense since neither one could get a genre or mood bonus to clearly separate itself from the other, so without that dominant boost, the system fell back almost entirely on closeness scoring, and the results felt more like a coin flip between similar-ish songs than a confident recommendation; the genre-trap and extreme-boundary profiles, both meant to see if the system could be fooled by unusual or extreme preferences, still returned a coherent top pick in both cases ("City of Sparks" for the genre-trap profile, "Coffee Shop Stories" for the extreme-boundary one), but the scores were noticeably lower across the board, topping out around 5.8 to 6.7 instead of 9+, which suggests the system handled the edge cases gracefully rather than breaking, it just couldn't find as strong a match, which is the expected and honestly correct behavior; and overall, comparing all six profiles side by side, the biggest thing that stood out was how consistent the "cliff" pattern was, one strong genre/mood match, then a cluster of closeness-only songs bunched together, which told me the scoring system is working as designed, even under pressure from adversarial profiles, but it also confirmed the bias I noted above: without a genre match, the system has a hard time meaningfully ranking songs against each other.
Example top-5 results for the tested profiles:

- House / electronic:
  1. City of Sparks (house, energetic) - 9.89
  2. Gym Hero (pop, intense) - 3.87
  3. Golden Hour Drive (disco, joyful) - 3.79
  4. Neon Alley (hip hop, confident) - 3.75
  5. Sunrise City (pop, happy) - 3.69

- Chill / lo-fi:
  1. Library Rain (lofi, chill) - 9.53
  2. Midnight Coding (lofi, chill) - 9.23
  3. Focus Flow (lofi, focused) - 7.37
  4. Spacewalk Thoughts (ambient, chill) - 5.80
  5. Quiet Harbor (ambient, dreamy) - 3.81

- Deep / intense rock:
  1. Storm Runner (rock, intense) - 9.40
  2. Gym Hero (pop, intense) - 4.82
  3. Night Drive Loop (synthwave, moody) - 3.36
  4. Neon Alley (hip hop, confident) - 3.06
  5. Sunrise City (pop, happy) - 3.02

- Conflicted energy profile:
  1. Sunrise City (pop, happy) - 7.35
  2. Gym Hero (pop, intense) - 7.33
  3. Storm Runner (rock, intense) - 3.59
  4. Night Drive Loop (synthwave, moody) - 3.57
  5. Neon Alley (hip hop, confident) - 3.37

- Genre-trap profile:
  1. City of Sparks (house, energetic) - 5.83
  2. Quiet Harbor (ambient, dreamy) - 3.47
  3. Spacewalk Thoughts (ambient, chill) - 3.44
  4. Winter Orchard (folk, dreamy) - 3.37
  5. Coffee Shop Stories (jazz, relaxed) - 3.31

- Extreme-boundary profile:
  1. Coffee Shop Stories (jazz, relaxed) - 6.74
  2. Quiet Harbor (ambient, dreamy) - 4.92
  3. Winter Orchard (folk, dreamy) - 4.64
  4. Spacewalk Thoughts (ambient, chill) - 2.93
  5. After the Rain (classical, melancholic) - 2.73

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
