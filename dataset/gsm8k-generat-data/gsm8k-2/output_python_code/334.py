def solution():
    """Eve wants to buy her 3 nieces cooking gear that's made for kids. The hand mitts cost $14.00 and the apron is $16.00. A set of 3 cooking utensils is $10.00 and a small knife is twice the amount of the utensils. The store is offering a 25% off sale on all cooking gear. How much will Eve spend on the gifts?"""
    hand_mitts = 14
    apron = 16
    utensils = 10
    knife = 2 * utensils
    total_cost = hand_mitts + apron + (utensils * 3) + knife
    discount = 0.25 * total_cost
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())