def solution():
    """Tyler wants to buy a dictionary that costs $18, a dinosaur book that costs $13, and a children's cookbook that costs $8. He has saved $14 from his allowance. If Tyler earns $5 per hour, how many hours does he have to work to afford his books?"""
    total_cost = 18 + 13 + 8
    saved_amount = 14
    remaining_amount = total_cost - saved_amount
    hourly_wage = 5
    hours_needed = remaining_amount / hourly_wage
    result = hours_needed
    return result

print(solution())