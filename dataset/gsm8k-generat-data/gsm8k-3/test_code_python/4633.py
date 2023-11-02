def solution():
    """Toby is dining out with his friend. They each order a cheeseburger for $3.65. He gets a milkshake for $2 and his friend gets a coke for $1. They split a large fries that cost $4. His friend also gets three cookies that cost $.5 each. The tax is $.2. They agree to split the bill. If Toby arrived with $15, how much change is he bringing home?"""
    # Define the cost of each item
    cheeseburger_cost = 3.65
    milkshake_cost = 2
    coke_cost = 1
    fries_cost = 4
    cookie_cost = 0.5
    tax = 0.2

    # Calculate the total cost of Toby's items
    toby_total = cheeseburger_cost + milkshake_cost + (0.5 * fries_cost) + (3 * cookie_cost)

    # Calculate the total cost of Toby's friend's items
    friend_total = cheeseburger_cost + coke_cost + (0.5 * fries_cost) + (3 * cookie_cost)

    # Calculate the total cost, including tax
    total_cost = (toby_total + friend_total) * (1 + tax)

    # Calculate the amount of change Toby will receive
    change = 15 - total_cost

    # Return the amount of change
    result = change
    return result

print(solution())