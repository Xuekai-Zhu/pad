def solution():
    # Calculate the total revenue Samantha needs to make to recover her capital
    capital = 5  # cost of the crate of eggs
    revenue_needed = capital / 0.2  # selling price of each egg is 20 cents

    # Calculate the number of eggs Samantha will sell before recovering her capital
    eggs_sold = revenue_needed / 30

    # Calculate the number of eggs Samantha will have left
    eggs_left = 30 - eggs_sold
    result = eggs_left
    return result

print(solution())