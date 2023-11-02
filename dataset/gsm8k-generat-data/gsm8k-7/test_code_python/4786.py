def solution():
    eggs_per_chocolate_cake = 3
    eggs_per_cheesecake = 8
    num_chocolate_cakes = 5
    num_cheesecakes = 9

    # Calculate the total number of eggs needed for 5 chocolate cakes
    total_eggs_for_chocolate_cakes = eggs_per_chocolate_cake * num_chocolate_cakes

    # Calculate the total number of eggs needed for 9 cheesecakes
    total_eggs_for_cheesecakes = eggs_per_cheesecake * num_cheesecakes

    # Calculate the difference in eggs needed between 9 cheesecakes and 5 chocolate cakes
    eggs_difference = total_eggs_for_cheesecakes - total_eggs_for_chocolate_cakes
    result = eggs_difference
    return result

print(solution())