def solution():
    # Calculate the total number of cartons of berries needed
    total_cartons = 42
    # Calculate the number of cartons Emilia already has
    already_have = 2 + 7
    # Calculate the number of cartons Emilia needs to buy
    cartons_to_buy = total_cartons - already_have
    result = cartons_to_buy
    return result

print(solution())