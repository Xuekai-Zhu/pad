def solution():
    # Calculate the number of eggs the chef used to make cakes
    eggs_for_cakes = 60 - 10  # the chef puts 10 eggs in the fridge, uses the rest for cakes
    num_cakes = eggs_for_cakes // 5  # 5 eggs are used to make one cake
    result = num_cakes
    return result

print(solution())