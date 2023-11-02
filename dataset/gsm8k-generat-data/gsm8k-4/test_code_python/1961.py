def solution():
    """The chocolate factory produces 50 candies per hour. It has to fulfill an order and produce 4000 candies. How many days will it take to complete the order if the factory works for 10 hours every day?"""
    # Define the production rate and the order quantity
    production_rate = 50
    order_quantity = 4000

    # Define the hours per day the factory works
    hours_per_day = 10

    # Calculate the total hours needed to fulfill the order
    total_hours = order_quantity / production_rate

    # Calculate the number of days needed to fulfill the order
    days_needed = total_hours / hours_per_day

    # Round up to the nearest day
    days_needed = math.ceil(days_needed)
    
    result = days_needed
    return result

print(solution())