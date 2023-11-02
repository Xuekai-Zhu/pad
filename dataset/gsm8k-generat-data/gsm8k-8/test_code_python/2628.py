def solution():
    # Calculate John's total budget from his grandparents
    total_budget = 50 * 4

    # Calculate the number of birds John can buy
    num_birds = total_budget / 20

    # Calculate the total number of wings from all the birds
    total_wings = num_birds * 2

    result = total_wings
    return result

print(solution())