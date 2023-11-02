def solution():
    """On a particular week, Fatima's restaurant served 25 people food and drinks, and 3/5 of that number came to buy coffee. How many people did not buy coffee in the restaurant?"""
    total_customers = 25
    coffee_customers = int(total_customers * (3/5))
    non_coffee_customers = total_customers - coffee_customers
    result = non_coffee_customers
    return result

print(solution())