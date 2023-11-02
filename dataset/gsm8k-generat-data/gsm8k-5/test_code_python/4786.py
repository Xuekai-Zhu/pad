def solution():
    eggs_per_chocolate_cake = 3  # 3 eggs are needed for one chocolate cake
    eggs_per_cheesecake = 8  # 8 eggs are needed for one cheesecake
    num_chocolate_cakes = 5  # 5 chocolate cakes are needed
    num_cheesecakes = 9  # 9 cheesecakes are needed

    # Calculate the total number of eggs needed for 5 chocolate cakes
    eggs_for_chocolate_cakes = eggs_per_chocolate_cake * num_chocolate_cakes

    # Calculate the total number of eggs needed for 9 cheesecakes
    eggs_for_cheesecakes = eggs_per_cheesecake * num_cheesecakes

    # Calculate the difference between the number of eggs needed for 9 cheesecakes and 5 chocolate cakes
    eggs_difference = eggs_for_cheesecakes - eggs_for_chocolate_cakes
    result = eggs_difference
    return result

print(solution())