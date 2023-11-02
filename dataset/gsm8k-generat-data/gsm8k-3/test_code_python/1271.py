def solution():
    """Dorothy is 15 years old and wants to go to a museum with her family. Her family consists of her, her younger brother, her parents, and her grandfather. The regular ticket cost is $10. People 18 years old or younger have a discount of 30%. How much money will Dorothy have after this trip, when she currently has $70?"""
    # Define the ticket price and discount percentage
    TICKET_PRICE = 10
    DISCOUNT_PERCENTAGE = 0.3

    # Define the number of people in Dorothy's family
    family_size = 5

    # Calculate the number of tickets Dorothy needs to buy
    if Dorothy.age <= 18:
        num_tickets = family_size * 0.7
    else:
        num_tickets = family_size

    # Calculate the total cost of the tickets
    total_cost = num_tickets * TICKET_PRICE

    # Calculate how much money Dorothy will have left after the trip
    money_left = Dorothy.money - total_cost

    result = money_left
    return result

print(solution())