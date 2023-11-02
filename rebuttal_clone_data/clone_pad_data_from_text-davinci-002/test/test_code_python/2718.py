def solution():
    eggs_per_chocolate_cake = 3
    eggs_per_cheesecake = 8
    chocolate_cakes = 5
    cheesecakes = 9
    chocolate_cake_eggs = eggs_per_chocolate_cake * chocolate_cakes
    cheesecake_eggs = eggs_per_cheesecake * cheesecakes
    total_eggs_needed = cheesecake_eggs - chocolate_cake_eggs
    result = total_eggs_needed
    return result

print(solution())