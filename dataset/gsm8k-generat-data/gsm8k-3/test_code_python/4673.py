def solution():
    """Leon ordered 3 sets of toy organizers for $78 per set and 2 gaming chairs for $83 each. If there is a delivery fee that is 5% of the total sales, how much did Leon pay?"""
    # Define the cost of each item
    TOY_ORGANIZER_COST = 78
    GAMING_CHAIR_COST = 83

    # Define the number of items purchased
    toy_organizer_sets = 3
    gaming_chairs = 2

    # Calculate the total cost of the toy organizers
    toy_organizer_cost = toy_organizer_sets * TOY_ORGANIZER_COST

    # Calculate the total cost of the gaming chairs
    gaming_chair_cost = gaming_chairs * GAMING_CHAIR_COST

    # Calculate the subtotal
    subtotal = toy_organizer_cost + gaming_chair_cost

    # Calculate the delivery fee
    delivery_fee = subtotal * 0.05

    # Calculate the total cost
    total_cost = subtotal + delivery_fee

    # Display the total cost
    result = total_cost
    return result

print(solution())