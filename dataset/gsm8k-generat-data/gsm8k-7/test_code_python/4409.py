def solution():
    num_cases = 15
    tins_per_case = 24
    damaged_percentage = 0.05

    # Calculate the total number of tins of beans delivered
    total_tins = num_cases * tins_per_case

    # Calculate the number of damaged tins
    num_damaged_tins = total_tins * damaged_percentage

    # Calculate the number of tins left after the damaged ones are thrown away
    num_tins_left = total_tins - num_damaged_tins
    result = num_tins_left
    return result

print(solution())