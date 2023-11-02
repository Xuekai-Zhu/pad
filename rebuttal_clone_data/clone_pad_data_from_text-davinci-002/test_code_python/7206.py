def solution():
    total_chocolates = 28
    chocolates_eaten_with_nuts = total_chocolates / 2
    chocolates_eaten_without_nuts = total_chocolates / 4
    total_chocolates_eaten = chocolates_eaten_with_nuts + chocolates_eaten_without_nuts
    result = total_chocolates_eaten
    return result

print(solution())