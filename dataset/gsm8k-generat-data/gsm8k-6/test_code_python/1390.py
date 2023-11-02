def solution():
    # Calculate the total cost of Nancy's coffee after 20 days
    daily_cost = 3 + 2.5  # cost of double espresso and iced coffee
    total_days = 20
    total_coffees = 2 * total_days
    total_cost = daily_cost * total_coffees
    result = total_cost
    return result

print(solution())