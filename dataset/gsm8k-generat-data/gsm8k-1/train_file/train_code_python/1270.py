def solution():
    """Dorothy is 15 years old and wants to go to a museum with her family. Her family consists of her, her younger brother, her parents, and her grandfather. The regular ticket cost is $10. People 18 years old or younger have a discount of 30%. How much money will Dorothy have after this trip, when she currently has $70?"""
    ticket_cost = 10
    family_members = 5
    discounted_ticket_cost = ticket_cost * 0.7
    total_discounted_cost = family_members * discounted_ticket_cost
    total_cost = family_members * ticket_cost
    total_savings = total_cost - total_discounted_cost
    current_money = 70
    remaining_money = current_money - total_discounted_cost
    result = remaining_money
    return result

print(solution())