# PokeDex
## Tech Stack
- Jupyter Notebook
- Flask/Python
- HTML/CSS/JS
## Functionalities 
- Home Page allows to search pokemon based on **Name**, **Type** and **Generation**.
- Pokemon guesser using image works like a real pokedex. Upload an image to the guesser or take one. And it will guess the **closest** pokemon(Trained for the first 151 pokemon only).
- Pokemon guesser using text tries to guess a pokemon using a pokemon description provided to it. The description is matched to the **closest** pokedex entry from all generations(Trained for the first 151 pokemon only).
- Pokemon Team Strength Ranker is an algorithm that ranks a given team. How the algorithm works:
  - Overall the strength of the team depends on the type coverage as the stats can vary based on Level, IV's, Nature, etc. But type remains constant for all the teams.
  - Strength of the team is greater if the type coverage in terms of attack is wide.
  - Also higher the immunities to other types or resistant to other types better the strength.
  - If weakness can be covered by other team members, the strength increases.
  - If team is 4X weak to certain types, the strength decreases.
