def solution():
    meal_cost = 15.00  # The cost of the customer's meal is $15.00
    tax_rate = 0.20  # The state applies a 20% tax to restaurant sales
    total_cost = meal_cost + (meal_cost * tax_rate)  # Calculate the total cost with tax
    payment = 20.00  # The customer gives Jason a $20 bill
    change = payment - total_cost  # Calculate the amount of change the customer should receive
    tip = change  # Jason's tip is the amount of change
    result = tip
    return result

print(solution())