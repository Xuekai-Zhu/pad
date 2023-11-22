def solution():
    
    # Define the regular price per blouse and the discount percentage
    REGULAR_PRICE = 20
    DISCOUNT_PERCENTAGE = 0.3

    # Calculate the discounted price per blouse
    discounted_price = REGULAR_PRICE * (1 - DISCOUNT_PERCENTAGE/100)

    # Calculate the total cost of the discounted blouses
    total_cost = discounted_price * 4

    # Display the total cost
    result = total_cost
    return result

print(solution())