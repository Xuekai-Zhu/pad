def solution():
    # Calculate the number of handfuls Susan has to pick before filling up her basket
    berries_left = 60
    handfuls_left = berries_left // 4  # Out of every handful of 5 strawberries she eats 1, so effectively she picks only 4
    # Calculate the total number of berries she has to pick
    total_beries = handfuls_left * 5
    result = total_beries
    return result

print(solution())