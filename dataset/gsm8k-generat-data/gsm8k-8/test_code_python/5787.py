def solution():
    # Define the initial price of apples and the new price after the increase
    initial_price = 1.6
    increase_percent = 25
    new_price = initial_price * (1 + increase_percent/100)

    # Calculate the total cost of 2 pounds of apples for one person
    amount_of_apples = 2  # in pounds
    cost_per_person = new_price * amount_of_apples

    # Calculate the total cost for the entire family
    num_people = 4
    total_cost = cost_per_person * num_people
    result = total_cost
    return result

print(solution())