def solution():
    # Define the initial amount of money Fred had and the amount he had left after buying the books
    initial_money = 236
    money_left = 14

    # Calculate the total cost of the books
    total_cost = initial_money - money_left

    # Calculate the average cost per book
    average_cost_per_book = total_cost / 6
    result = average_cost_per_book
    return result

print(solution())