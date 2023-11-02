def solution():
    """James bought a gallon of milk for $3, a bunch of bananas for $2, and paid 20% sales tax. How much money did James spend?"""
    # Define the prices of the items
    milk_price = 3
    banana_price = 2

    # Calculate the total before tax
    total = milk_price + banana_price

    # Calculate the amount of tax
    tax_percent = 0.2
    tax = total * tax_percent

    # Calculate the total with tax
    total_with_tax = total + tax

    # Display the total spent
    result = total_with_tax
    return result

print(solution())