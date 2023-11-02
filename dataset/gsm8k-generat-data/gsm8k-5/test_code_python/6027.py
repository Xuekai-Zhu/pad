def solution():
    eggs_before = 10  # The family had 10 eggs before
    eggs_used = 5  # The mother used 5 eggs to make an omelet
    eggs_after = eggs_before - eggs_used  # The family has this many eggs left

    # Calculate how many eggs the chickens laid and add it to the previous count
    eggs_chickens_laid = 2 * 3  # 2 chickens laid 3 eggs each
    eggs_now = eggs_after + eggs_chickens_laid
    result = eggs_now
    return result

print(solution())