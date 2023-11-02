def solution():
    total_nuts = 30  # There are 30 different nuts in the bowl
    eaten_nuts = (5/6) * total_nuts  # 5/6 of the nuts were eaten
    remaining_nuts = total_nuts - eaten_nuts  # Calculate the number of nuts left

    result = remaining_nuts
    return result

print(solution())