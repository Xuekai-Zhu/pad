def solution():
    # Calculate the amount of velvet needed for one cloak
    velvet_per_cloak = 3

    # Calculate the amount of velvet needed for one hat
    velvet_per_hat = 1/4

    # Calculate the total amount of velvet needed for 6 cloaks
    total_cloak_velvet = velvet_per_cloak * 6

    # Calculate the total amount of velvet needed for 12 hats
    total_hat_velvet = velvet_per_hat * 12

    # Calculate the total amount of velvet needed for 6 cloaks and 12 hats
    total_velvet = total_cloak_velvet + total_hat_velvet

    result = total_velvet
    return result

print(solution())