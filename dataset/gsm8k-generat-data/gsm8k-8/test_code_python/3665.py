def solution():
    # Define the cost of each item in cents
    candy_bar_cost = 25
    chocolate_cost = 75
    juice_cost = 50

    # Calculate the total cost of the items in cents
    total_cost = (3 * candy_bar_cost) + (2 * chocolate_cost) + juice_cost

    # Since each quarter is worth 25 cents, calculate the number of quarters needed
    number_of_quarters = total_cost / 25

    result = number_of_quarters
    return result

print(solution())