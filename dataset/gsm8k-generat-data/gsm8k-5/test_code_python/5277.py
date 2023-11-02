def solution():
    total_apples = 34  # Isabel and her mom picked 34 apples
    ripe_apples = total_apples - 6  # 6 apples were not ripe
    apples_per_pie = 4  # Each apple pie needs 4 apples

    # Calculate the number of pies they can make with the ripe apples
    pies = ripe_apples // apples_per_pie
    result = pies
    return result

print(solution())