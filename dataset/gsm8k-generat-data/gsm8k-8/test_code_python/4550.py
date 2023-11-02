def solution():
    # Define the cost per kilogram of cabbage
    cabbage_cost = 2

    # Calculate the total earnings from all three days
    total_earnings = 30 + 24 + 42

    # Divide the total earnings by the cost per kilogram to find kilograms sold
    kilograms_sold = total_earnings / cabbage_cost
    result = kilograms_sold
    return result

print(solution())