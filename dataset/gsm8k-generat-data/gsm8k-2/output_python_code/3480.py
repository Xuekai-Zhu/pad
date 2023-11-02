def solution():
    """Miriam currently has 30 marbles, but she used to have more. Miriam gave her brother 60 marbles, gave her sister twice that amount and gave her friend Savanna three times the amount she currently has. How many marbles did Miriam start with?"""
    savanna_marbles = 3 * 30
    sister_marbles = 2 * 60
    total_given_away = 60 + sister_marbles + savanna_marbles
    starting_marbles = 30 + total_given_away
    result = starting_marbles
    return result

print(solution())