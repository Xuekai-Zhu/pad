def solution():
    yesterday_drink = 48
    percent_less = 0.04  # 4% less

    # Calculate the original (two days ago) amount of water Tony drank
    original_drink = yesterday_drink / (1 - percent_less) 

    result = original_drink
    return result

print(solution())