def solution():
    # Calculate the total cost of food and drinks
    food_cost = 80
    drink_cost = 10
    total_cost = food_cost + drink_cost

    # Calculate the sales tax
    sales_tax = 0.1 * total_cost

    # Calculate the total bill
    total_bill = total_cost + sales_tax

    # Calculate the gratuity amount
    gratuity = total_bill - 140

    result = gratuity
    return result

print(solution())