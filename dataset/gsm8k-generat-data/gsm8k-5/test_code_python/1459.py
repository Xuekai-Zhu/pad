def solution():
    # Calculate the total amount of coffee James needs to buy each day
    coffee_per_person_per_day = 2 * 0.5  # 2 cups per person per day, and 0.5 ounces of coffee per cup
    total_coffee_per_day = coffee_per_person_per_day * 4  # James is buying coffee for 4 people in the house
    total_coffee_per_week = total_coffee_per_day * 7  # James needs to buy enough coffee for a week

    # Calculate the total cost of the coffee
    cost_per_ounce = 1.25  # Coffee costs $1.25 per ounce
    total_cost = total_coffee_per_week * cost_per_ounce

    result = total_cost
    return result

print(solution())