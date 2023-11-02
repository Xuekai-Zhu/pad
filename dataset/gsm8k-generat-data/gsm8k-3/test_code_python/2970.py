def solution():
    """Marlon had 30 female baby bunnies in his hutch. They matured after four months, and he gave 2/5 of them to his friend Rodney. If after another three months the bunnies conceived and gave birth to 2 kittens each, calculate the total number of bunnies Marlon has in his hutch now."""
    # Define the initial number of bunnies
    initial_bunnies = 30

    # Calculate the number of bunnies matured after 4 months
    matured_bunnies = initial_bunnies
    # Calculate the number of bunnies gifted to Rodney
    gifted_bunnies = 2/5 * matured_bunnies
    # Calculate the number of bunnies remaining with Marlon
    remaining_bunnies = matured_bunnies - gifted_bunnies

    # Calculate the number of kittens per bunny after giving birth
    kittens_per_bunny = 2

    # Calculate the total number of bunnies after giving birth
    total_bunnies = remaining_bunnies + remaining_bunnies * kittens_per_bunny

    # Display the total number of bunnies
    result = total_bunnies
    return result

print(solution())