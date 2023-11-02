def solution():
    """Miriam currently has 30 marbles, but she used to have more. Miriam gave her brother 60 marbles, gave her sister twice that amount and gave her friend Savanna three times the amount she currently has. How many marbles did Miriam start with?"""
    current_marbles = 30
    brother_marbles = 60
    sister_marbles = 2 * brother_marbles
    savanna_marbles = 3 * current_marbles
    total_marbles = current_marbles + brother_marbles + sister_marbles + savanna_marbles
    result = total_marbles

    return result

print(solution())