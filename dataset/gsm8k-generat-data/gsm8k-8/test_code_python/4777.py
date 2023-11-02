def solution():
    # Define the given information
    discount_percent = 0.25
    additional_discount_percent = 1/3
    threshold = 5
    original_price = 20
    chairs_bought = 8

    # Calculate the discounted price per chair
    discounted_price = original_price - (original_price * discount_percent)

    # Determine how many chairs are eligible for additional discount
    eligible_chairs = max(chairs_bought - threshold, 0)

    # Calculate the additional discount
    additional_discount = discounted_price * additional_discount_percent * eligible_chairs

    # Calculate the total cost of the chairs
    total_cost = (original_price * chairs_bought) - ((discounted_price * (chairs_bought - eligible_chairs)) + additional_discount)

    result = total_cost
    
    return result

print(solution())