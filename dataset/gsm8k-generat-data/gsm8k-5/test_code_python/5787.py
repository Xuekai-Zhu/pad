def solution():
    initial_price = 1.6  # Apples originally cost $1.6 per pound
    price_increase = 0.25  # The price got raised by 25%
    new_price = initial_price * (1 + price_increase)  # Calculate the new price
    pounds_per_person = 2  # Each person in the family wants to buy 2 pounds of apples
    family_size = 4  # The family has 4 members

    # Calculate the total cost for the family to buy 2 pounds of apples per person
    total_cost = new_price * pounds_per_person * family_size
    result = total_cost
    return result

print(solution())