def solution():
    # Calculate the total number of eggs required for 5 chocolate cakes and 9 cheesecakes
    eggs_for_5_chocolate_cakes = 3 * 5  # each chocolate cake needs 3 eggs
    eggs_for_9_cheesecakes = 8 * 9  # each cheesecake needs 8 eggs
    # Calculate the difference between the two
    egg_difference = eggs_for_9_cheesecakes - eggs_for_5_chocolate_cakes
    result = egg_difference
    return result

print(solution())