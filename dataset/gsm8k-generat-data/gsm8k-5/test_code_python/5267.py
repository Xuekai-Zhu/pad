def solution():
    milk_price = 3  # James bought a gallon of milk for $3
    banana_price = 2  # James bought a bunch of bananas for $2
    sales_tax = 0.2  # James paid 20% sales tax

    # Calculate the total cost before tax
    total_cost_before_tax = milk_price + banana_price

    # Calculate the total cost after tax
    total_cost_after_tax = total_cost_before_tax + (total_cost_before_tax * sales_tax)

    result = total_cost_after_tax
    return result

print(solution())