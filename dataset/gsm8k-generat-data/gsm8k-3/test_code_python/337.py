def solution():
    """Eve wants to buy her 3 nieces cooking gear that's made for kids.  The hand mitts cost $14.00 and the apron is $16.00.  A set of 3 cooking utensils is $10.00 and a small knife is twice the amount of the utensils.  The store is offering a 25% off sale on all cooking gear.  How much will Eve spend on the gifts?"""
    # Define the cost of each item
    HAND_MITTS_COST = 14
    APRON_COST = 16
    UTENSILS_COST = 10
    KNIFE_COST = UTENSILS_COST * 2

    # Calculate the total cost before discount
    total_cost = (HAND_MITTS_COST + APRON_COST + UTENSILS_COST + KNIFE_COST) * 3

    # Apply the 25% discount
    discounted_cost = total_cost * 0.75

    # Display the final cost
    result = discounted_cost
    return result

print(solution())