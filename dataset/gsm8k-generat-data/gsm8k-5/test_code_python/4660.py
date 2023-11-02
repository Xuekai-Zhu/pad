def solution():
    car_cost = 14600  # The cost of the new car is $14600
    current_savings = 14500  # Alex already has $14500 saved up
    trips = 40  # Alex plans to make 40 grocery trips to save up the rest of the money
    cost_per_trip = 1.5  # Alex charges $1.5 per trip
    grocery_percentage = 0.05  # Alex charges 5% of the price of the groceries

    # Calculate the remaining amount of money needed to buy the car
    remaining_amount = car_cost - current_savings

    # Calculate the total amount of money earned from delivering groceries
    total_earned = trips * (cost_per_trip + grocery_percentage * remaining_amount)

    # Calculate the total amount of money earned only from delivering groceries
    grocery_earnings = total_earned - remaining_amount

    result = grocery_earnings
    return result

print(solution())