def solution():
    # Calculate the total amount spent on crayons, books, and calculators
    total_spent = 5 * 5 + 10 * 5 + 3 * 5

    # Calculate the amount of change Bruce has
    change = 200 - total_spent

    # Calculate the number of bags he can buy with the change
    num_bags = change // 10

    result = num_bags
    return result

print(solution())