def solution():
    # Calculate the total price for the family's entrance tickets
    total_tickets_price = 5 * 6  # 6 people in total

    # Calculate the price for one attraction for the kids and parents
    attraction_price = 4 + 2 * 4  # 4 kids and 2 parents

    # Add the attraction price to the total tickets price
    total_price = total_tickets_price + attraction_price

    # Add the grandmother's ticket price (she gets in for free)
    total_price += 5

    result = total_price
    return result

print(solution())