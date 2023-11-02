def solution():
    total_apples = 34
    ripe_apples = total_apples - 6
    apples_per_pie = 4

    # Calculate the number of pies they can make with ripe apples
    pies = ripe_apples // apples_per_pie
    result = pies
    return result

print(solution())