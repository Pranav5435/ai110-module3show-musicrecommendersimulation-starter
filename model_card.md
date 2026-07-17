# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
BeatMatch 1.0. I wanted something that nodded to the fact that my main test profile was house/electronic, and "beatmatch" is literally a DJ term for lining tracks up so they flow together, which felt like a fitting metaphor for a system that's trying to line up songs with a listener's taste. The 1.0 is there to make it feel like a real first release instead of a rough draft, even though under the hood it's still a simple weighted scoring script.
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  
BeatMatch 1.0 is built for someone who already has a clear, strong sense of what they want to hear, a specific genre and mood they're locked into, not someone browsing with vague or mixed tastes. It's designed to run on a small catalog for simulation and demo purposes, not anything close to production scale. The whole point of the project is to demonstrate how content-based scoring works in practice, how a system can take a user's stated preferences and a handful of song features and turn that into a ranked list, not to function as an actual streaming product. It's not meant to be used with a real user base or in a production app, mainly because the bias I found in testing shows it leans hard on genre and mood matching, which means it would likely trap real users in a narrow bubble of results rather than actually learning their taste over time. It also shouldn't be trusted for users with mixed or ambiguous preferences, since my conflicted energy profile test showed the scoring logic doesn't know what to do when the inputs contradict each other, it just kind of guesses based on whichever feature happens to line up. Because of that, this should never be treated as a sole recommender. At best it's one signal among many that a real system would combine with other signals before actually deciding what to recommend.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.
Every song in the catalog gets evaluated on six features: genre, mood, energy, balance, danceability, and acousticness. The user side works off the exact same six features, just expressed as targets and favorites instead of fixed values, so a user has a favorite_genre and favorite_mood plus target_energy, target_balance, target_danceability, and target_acousticness. To turn all of that into a single score, genre and mood work as fixed bonuses, if a song's genre matches the user's favorite genre it gets a flat +4.0, and a mood match adds +2.0. The other four features aren't binary like that, they're scored based on how close the song's actual value is to what the user is targeting, up to +1.0 each, so a song doesn't need to hit the target exactly to get credit, it just needs to be close. All six of those numbers then get added together into one final score, which is what determines the ranking. What changed from the starter logic is that I didn't stick to just genre, mood, and energy. I added balance, danceability, and acousticness as additional features the starter code didn't include, which gave the scoring system a lot more to work with when telling songs apart. I also moved away from the default starter weighting and picked my own specific numbers, genre at +4.0, mood at +2.0, and the four closeness features capped at +1.0 each, instead of just using whatever the starter values were.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  
Starting from the 10 song starter catalog, I added new songs during Phase 2 to cover a wider range of styles, bringing the total up to 18 songs in songs.csv. Across my test runs, the genres and moods represented ended up spanning house, lofi, ambient, rock, pop, synthwave, folk, jazz, classical, hip hop, and disco, so I did make sure my expanded dataset didn't just double down on house and electronic. Yes, I added new data on top of the starter set specifically to cover genres and moods that weren't already there, roughly 8 new songs beyond the original 10. What's still missing is anything from metal, country, reggae, or world/international music, genres that obviously exist in real music but never once showed up across any of my test profiles or outputs, which is a real gap in how broadly this system could actually generalize.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  
The user type that gets the best results out of this system is someone like my house/electronic profile, since it produced the clearest single winner in any of my tests, City of Sparks at 9.89, with a huge separation from every other song in the results. That's the system working exactly as designed when a user's preferences are specific and consistent. The scoring also captures a different kind of pattern well, shown by my lofi profile results, where instead of one dominant winner, multiple songs scored above 7.0. That tells me the system correctly recognized several songs as genuinely close matches rather than just surfacing one lucky hit, which is a good sign that the closeness scoring on the non-genre features is actually doing real work, not just riding on the genre bonus. One of the clearest moments where a recommendation matched my own gut was that same City of Sparks result, it felt like the obviously right pick for my house profile before I'd even looked at the score breakdown, and then the system backed that up with a 9.89 that blew every other song out of the water. That's a real example of the system's output lining up with my own musical intuition on a clear-cut case, which is exactly what you'd want to see before trusting it on messier ones.
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

```
House / electronic:
  1. City of Sparks (house, energetic) - 9.89
  2. Gym Hero (pop, intense) - 3.87
  3. Golden Hour Drive (disco, joyful) - 3.79
  4. Neon Alley (hip hop, confident) - 3.75
  5. Sunrise City (pop, happy) - 3.69

Chill / lo-fi:
  1. Library Rain (lofi, chill) - 9.53
  2. Midnight Coding (lofi, chill) - 9.23
  3. Focus Flow (lofi, focused) - 7.37
  4. Spacewalk Thoughts (ambient, chill) - 5.80
  5. Quiet Harbor (ambient, dreamy) - 3.81

Deep / intense rock:
  1. Storm Runner (rock, intense) - 9.40
  2. Gym Hero (pop, intense) - 4.82
  3. Night Drive Loop (synthwave, moody) - 3.36
  4. Neon Alley (hip hop, confident) - 3.06
  5. Sunrise City (pop, happy) - 3.02

Conflicted energy profile:
  1. Sunrise City (pop, happy) - 7.35
  2. Gym Hero (pop, intense) - 7.33
  3. Storm Runner (rock, intense) - 3.59
  4. Night Drive Loop (synthwave, moody) - 3.57
  5. Neon Alley (hip hop, confident) - 3.37

Genre-trap profile:
  1. City of Sparks (house, energetic) - 5.83
  2. Quiet Harbor (ambient, dreamy) - 3.47
  3. Spacewalk Thoughts (ambient, chill) - 3.44
  4. Winter Orchard (folk, dreamy) - 3.37
  5. Coffee Shop Stories (jazz, relaxed) - 3.31

Extreme-boundary profile:
  1. Coffee Shop Stories (jazz, relaxed) - 6.74
  2. Quiet Harbor (ambient, dreamy) - 4.92
  3. Winter Orchard (folk, dreamy) - 4.64
  4. Spacewalk Thoughts (ambient, chill) - 2.93
  5. After the Rain (classical, melancholic) - 2.73
```

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  
The biggest fix I'd want to make is smoothing out the scoring cliff I found, where genre and mood matches add a flat bonus instead of a scaled one, which creates a huge gap between songs that match the genre and everything else, even when the "everything else" songs are actually really close on every other feature. Instead of an all-or-nothing bonus, I'd want genre and mood to contribute proportionally, almost like a similarity score instead of a binary switch, so a strong overall vibe match isn't automatically buried just because it's in a different genre. Second, I'd want to grow the dataset, both in raw size and in how many genres and moods are represented, since testing edge cases really exposed how thin the coverage was outside of house and adjacent styles. Last, going back to what I researched in Phase 1 about collaborative filtering versus content-based filtering, I'd want to actually add a collaborative filtering layer on top of this, so the system isn't only reasoning from a user's stated preferences but also from patterns across other users, which is closer to how real recommenders like Spotify actually work. 
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
My biggest learning moment was seeing the actual score gap in my real output, watching City of Sparks land at 9.89 while everything else clustered in the high 3s. It's one thing to read that genre and mood carry the most weight, it's another thing to see that translate into a nearly three-times score gap in practice. That was the moment the "bias" I'd written about in my README stopped being theoretical and started being something I could point to in my own terminal. AI was genuinely useful for implementation speed, and it also caught something I hadn't noticed myself, that pairing house music with low danceability in my user profile was internally inconsistent, since house is one of the most danceable genres there is. That was a good catch that saved me from building my whole test profile on a contradiction. But I also had to push back and verify things instead of just taking the first answer. When I considered moving to a 10-point scale to make scoring feel more precise, I had to stop and think about whether a bigger number range actually meant more accuracy, and it didn't, it just meant bigger numbers. I also made sure to land on my own genre versus mood weighting instead of just going with whatever the AI suggested first, because I wanted to be able to defend that decision as mine. What surprised me most was how much a simple weighted formula can still feel like a real recommendation when you're staring at the output, City of Sparks genuinely felt like the right pick for my profile before I even looked at the math behind it. The flip side of that surprise was how visible the bias became the moment I ran real data through it instead of just reasoning about it abstractly. It's easy to write "this might create a filter bubble" in a README, it's a different thing to watch it happen in your own terminal output. Going forward, I'd want to try smoothing out that scoring cliff first, since it's the most direct fix for the exact bias I saw, and then start layering in a basic collaborative filtering signal so the system has more than one way of understanding what "good" means for a given user.