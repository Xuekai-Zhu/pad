def solution():
    meal_cost = 80  # The cost of the NY Striploin is $80
    wine_cost = 10  # The cost of the glass of wine is $10
    subtotal = meal_cost + wine_cost  # The subtotal is the sum of the meal and wine cost
    tax_rate = 0.1  # The sales tax rate is 10%
    tax = subtotal * tax_rate  # The tax is calculated as the product of the subtotal and the tax rate
    total_cost = subtotal + tax  # The total cost is the sum of the subtotal and the tax
    gratuities = 140 - total_cost  # The gratuities are the difference between the total cost and the amount paid by the customer
    result = gratuities
    return result

print(solution())