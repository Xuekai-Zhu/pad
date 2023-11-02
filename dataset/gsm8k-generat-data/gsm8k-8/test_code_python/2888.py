def solution():
    # Calculate the cost of 3 liters of chlorine
    chlorine_price = 10 * 3
    chlorine_discount = chlorine_price * 0.2
    chlorine_cost = chlorine_price - chlorine_discount

    # Calculate the cost of 5 boxes of soap
    soap_price = 16 * 5
    soap_discount = soap_price * 0.25
    soap_cost = soap_price - soap_discount

    # Calculate the total cost and the cost after the discount
    total_cost = chlorine_cost + soap_cost
    cost_after_discount = (chlorine_price + soap_price) - (chlorine_discount + soap_discount)

    # Calculate the total savings
    total_savings = cost_after_discount - total_cost
    result = total_savings
    return result

print(solution())