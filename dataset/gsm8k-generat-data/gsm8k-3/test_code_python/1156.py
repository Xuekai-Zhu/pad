def solution():
    """A beadshop earns a third of its profit on Monday, a quarter of its profit on Tuesday and the rest of its profit on Wednesday. The shop makes a total profit of $1,200. How much profit, in dollars, was made on Wednesday?"""
    # Define the fractions of profits earned on Monday and Tuesday
    monday_fraction = 1/3
    tuesday_fraction = 1/4

    # Calculate the combined fraction of profits earned on Monday and Tuesday
    monday_tuesday_fraction = monday_fraction + tuesday_fraction

    # Calculate the fraction of profits earned on Wednesday
    wednesday_fraction = 1 - monday_tuesday_fraction

    # Calculate the profit made on Wednesday
    total_profit = 1200
    wednesday_profit = wednesday_fraction * total_profit

    # Display the profit made on Wednesday
    result = wednesday_profit
    return result

print(solution())