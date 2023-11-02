def solution():
    # Define the number of nights and the original cost per night
    nights = 3
    cost_per_night = 250

    # Calculate the total cost before the discount
    before_discount = nights * cost_per_night

    # Apply the discount
    after_discount = before_discount - 100

    # Return the final cost
    result = after_discount
    return result

print(solution())