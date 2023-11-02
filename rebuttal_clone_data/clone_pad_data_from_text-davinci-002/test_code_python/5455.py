def solution():
    total_chocolates = 24
    chocolates_eaten_1 = 4
    chocolates_eaten_2 = 3 + (2 * chocolates_eaten_1)
    chocolates_eaten_3 = chocolates_eaten_1 + 2
    chocolates_eaten_4 = chocolates_eaten_3 + 1
    chocolates_eaten_5 = chocolates_eaten_4 + 1
    total_chocolates_eaten = chocolates_eaten_1 + chocolates_eaten_2 + chocolates_eaten_3 + chocolates_eaten_4 + chocolates_eaten_5
    chocolates_remaining = total_chocolates - total_chocolates_eaten
    result = chocolates_remaining
    return result

print(solution())