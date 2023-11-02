def solution():
    num_ducks_with_5_ducklings = 2
    num_ducklings_per_5_ducks = 5

    num_ducks_with_3_ducklings = 6
    num_ducklings_per_3_ducks = 3

    num_ducks_with_6_ducklings = 9
    num_ducklings_per_6_ducks = 6

    # Calculate the total number of ducks
    total_ducks = num_ducks_with_5_ducklings + num_ducks_with_3_ducklings + num_ducks_with_6_ducklings

    # Calculate the total number of ducklings
    total_ducklings = (num_ducks_with_5_ducklings * num_ducklings_per_5_ducks) + (num_ducks_with_3_ducklings * num_ducklings_per_3_ducks) + (num_ducks_with_6_ducklings * num_ducklings_per_6_ducks)

    # Calculate the total number of ducks and ducklings
    total = total_ducks + total_ducklings
    result = total
    return result

print(solution())