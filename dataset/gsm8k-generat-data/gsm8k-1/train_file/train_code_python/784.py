def solution():
    """On a particular week, Fatima's restaurant served 25 people food and drinks, and 3/5 of that number came to buy coffee. How many people did not buy coffee in the restaurant?"""
    total_people = 25
    coffee_buyers = total_people * 3/5
    non_coffee_buyers = total_people - coffee_buyers
    result = non_coffee_buyers
    return result

print(solution())