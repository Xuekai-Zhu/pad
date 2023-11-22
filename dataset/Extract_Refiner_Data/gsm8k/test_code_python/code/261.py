def solution():
    
    # Define the budget and the selling price of the property
    budget = 400000
    selling_price = 350000

    # Calculate the total price of the house
    total_price = selling_price * 1.05 + selling_price * 0.12

    # Calculate the difference between the total price and the budget
    difference = total_price - budget

    # Display the difference in price
    result = difference
    return result

print(solution())