def solution():
    # Calculate the total amount of strawberries picked
    total_strawberries = 10 + 2*10  # Rachel picked twice as much as Christine
    # Calculate the number of pies they can make
    num_pies = total_strawberries // 3  # they need 3 pounds of strawberries per pie
    result = num_pies
    return result

print(solution())