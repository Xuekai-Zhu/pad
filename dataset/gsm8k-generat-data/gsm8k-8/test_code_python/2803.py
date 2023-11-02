def solution():
    # Define Todd's initial amount of money
    todd_money = 20

    # Define the cost of each candy bar
    candy_bar_cost = 2

    # Calculate the total cost of the candy bars
    total_candy_bar_cost = candy_bar_cost * 4

    # Calculate Todd's remaining money after buying the candy bars
    remaining_money = todd_money - total_candy_bar_cost
    result = remaining_money
    return result

print(solution())