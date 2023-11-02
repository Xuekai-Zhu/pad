def solution():
    strawberries_per_pie = 3  # 3 pounds of strawberries needed per pie
    total_strawberries = 10 + 2 * 10  # Christine picked 10 pounds, and Rachel picked twice as much

    # Calculate the number of pies they can make
    pies = total_strawberries // strawberries_per_pie
    result = pies
    return result

print(solution())