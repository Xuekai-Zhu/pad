def solution():
    # Find the number of people in Dorothy's family
    num_people = 1 + 1 + 2 + 1  # Dorothy, younger brother, parents, grandfather

    # Find the total cost of the tickets without the discount
    total_cost = num_people * 10

    # Find the discount amount for Dorothy's ticket
    if Dorothy <= 18:
        discount = 0.3 * 10
    else:
        discount = 0

    # Subtract Dorothy's discount from the total cost
    total_cost -= discount

    # Calculate the amount of money Dorothy will have after the trip
    money_left = 70 - total_cost
    result = money_left
    return result

print(solution())