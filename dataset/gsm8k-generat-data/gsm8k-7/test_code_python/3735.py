def solution():
    num_cardinals = 3
    num_robins = 4 * num_cardinals
    num_blue_jays = 2 * num_cardinals
    num_sparrows = 3 * num_cardinals + 1

    # Calculate the total number of birds Camille saw
    total_birds = num_cardinals + num_robins + num_blue_jays + num_sparrows
    result = total_birds
    return result

print(solution())