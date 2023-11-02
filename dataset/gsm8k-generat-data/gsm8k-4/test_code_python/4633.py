def solution():
    """Toby is dining out with his friend. They each order a cheeseburger for $3.65. He gets a milkshake for $2
    and his friend gets a coke for $1. They split a large fries that cost $4. His friend also gets three 
    cookies that cost $.5 each. The tax is $.2. They agree to split the bill. If Toby arrived with $15, 
    how much change is he bringing home?"""
    
    # Define the cost of each item
    burger_cost = 3.65
    milkshake_cost = 2
    coke_cost = 1
    fries_cost = 4
    cookie_cost = 0.5
    tax = 0.2

    # Calculate the total cost of the meal
    total_cost = (burger_cost * 2) + milkshake_cost + coke_cost + fries_cost + (3 * cookie_cost) + tax

    # Calculate the amount each person needs to pay
    each_pay = total_cost / 2

    # Calculate the amount of change Toby has
    change = 15 - each_pay

    # Return the result
    result = round(change, 2)
    return result

print(solution())