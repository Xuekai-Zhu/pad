def solution():
    initial_amount = 30  # Hannah brought $30 to the county fair
    spent_on_rides = initial_amount / 2  # Hannah spent half of the initial amount on rides
    spent_on_dessert = 5  # Hannah spent $5 on dessert

    # Calculate the remaining amount
    remaining_amount = initial_amount - spent_on_rides - spent_on_dessert
    result = remaining_amount
    return result

print(solution())