def solution():
    """Marlon had 30 female baby bunnies in his hutch. They matured after four months, and he gave 2/5 of them to his friend Rodney. If after another three months the bunnies conceived and gave birth to 2 kittens each, calculate the total number of bunnies Marlon has in his hutch now."""
    # Define the initial number of female baby bunnies
    initial_bunnies = 30

    # Mature the female baby bunnies to adults
    mature_bunnies = initial_bunnies

    # Give 2/5 of the mature bunnies to Rodney
    rodney_bunnies = mature_bunnies * 2/5
    marlon_bunnies = mature_bunnies - rodney_bunnies

    # Calculate the number of bunnies after giving 2 kittens each
    new_bunnies = marlon_bunnies * 2
    total_bunnies = marlon_bunnies + new_bunnies
    
    result = total_bunnies
    return result

print(solution())