def solution():
    ticket_price = 8  # Movie tickets cost $8 per person
    total_money = 25  # The sisters brought $25 with them

    # Calculate the total cost of the movie tickets
    total_cost = 2 * ticket_price  # Two sisters are going to the movies

    # Calculate the change the sisters will receive after buying the tickets
    change = total_money - total_cost
    result = change
    return result

print(solution())