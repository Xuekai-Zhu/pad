def solution():
    # Define who developed the theory of evolution and if Pokemon rely on evolution
    darwin_developed_evolution = True
    pokemon_rely_on_evolution = True
    # Check if Pikachu would like Charles Darwin based on these facts
    if darwin_developed_evolution and pokemon_rely_on_evolution:
        result = "maybe"
    else:
        result = "no"
    return result

print(solution())