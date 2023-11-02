def solution():
    
    eggs_per_chocolate_cake = 3
    eggs_per_cheesecake = 8
    chocolate_cakes = 5
    cheesecakes = 9
    total_eggs_for_chocolate_cakes = chocolate_cakes * eggs_per_chocolate_cake
    total_eggs_for_cheesecakes = cheesecakes * eggs_per_cheesecake
    eggs_difference = total_eggs_for_cheesecakes - total_eggs_for_chocolate_cakes
    result = eggs_difference
    return result

print(solution())