def solution():
    """The chocolate factory produces 50 candies per hour. It has to fulfill an order and produce 4000 candies. How many days will it take to complete the order if the factory works for 10 hours every day?"""
    candies_per_hour = 50
    total_candies = 4000
    daily_production = candies_per_hour * 10
    days_to_complete_order = total_candies / daily_production
    result = days_to_complete_order
    return result

print(solution())