def solution():
    # Calculate the number of Rhode Island Reds in Britney's flock
    britney_rhode_island_reds = 2 * 11

    # Calculate the number of Golden Comets in Britney's flock
    britney_golden_comets = 6 / 2

    # Calculate the total number of chickens in Britney's flock
    britney_total_chickens = britney_rhode_island_reds + britney_golden_comets

    # Calculate the total number of chickens in Susie's flock
    susie_total_chickens = 11 + 6

    # Calculate the difference in number of chickens between the two flocks
    difference_in_chickens = britney_total_chickens - susie_total_chickens

    result = difference_in_chickens
    return result

print(solution())