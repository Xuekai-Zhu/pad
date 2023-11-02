def solution():
    
    # Define the prices of the loyalty card and the coupon
    COUPON_PRICE = 1
    COUPON_COUPON_PRICE = 2 * COUPON_PRICE

    # Define the amount spent by the last shopping trip
    last_shopping_trip_spending = 80

    # Calculate the amount spent on the second shopping trip
    second_shopping_trip_spending = last_shopping_trip_spending - 20

    # Calculate the number of rewards applied by the coupon
    coupon_rewards = second_shopping_trip_spending // COUPON_PRICE

    # Calculate the total cost of the shopping trip
    total_cost = second_shopping_trip_spending + coupon_rewards

    # Display the total cost
    result = total_cost
    return result

print(solution())