def solution():
    num_cars = 3
    car_price = 5
    total_earned = 45
    
    # Calculate the total earnings from selling the little cars
    cars_earned = num_cars * car_price
    
    # Calculate the cost of the Legos set by subtracting the earnings from the total amount earned
    legos_cost = total_earned - cars_earned
    result = legos_cost
    return result

print(solution())