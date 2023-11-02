def solution():
    # Define the total amount of kibble Luna should eat in one day
    daily_amount = 2

    # Define the amount of kibble Mary gave Luna
    mary_amount = 1 + 1

    # Define the amount of kibble Frank gave Luna
    frank_amount = 1 + (2 * 1)

    # Calculate the total amount of kibble Luna ate in one day
    total_amount = mary_amount + frank_amount

    # Calculate the amount of kibble left in the bag
    remaining_amount = 12 - total_amount

    result = remaining_amount
    return result

print(solution())