def solution():
    
    # Define the prices of the manicure and pedicure
    MANICURE_PRICE = 35
    PEDICURE_PRICE = 40

    # Calculate the total cost of the manicure and pedicure
    total_cost = MANICURE_PRICE + PEDICURE_PRICE

    # Calculate the discount for both manicures and pedicures
    discount = total_cost * 0.2
    discounted_cost = total_cost - discount

    # Calculate the cost per nail
    nail_price = 3

    # Calculate the total cost of nail art on both fingers
    total_cost += nail_price * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())