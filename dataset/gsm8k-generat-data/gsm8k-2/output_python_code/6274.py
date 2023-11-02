def solution():
    """Tanesha needs to buy rope so cut into 10 pieces that are each six inches long. She sees a 6-foot length of rope that cost $5 and also sees 1-foot lengths of rope that cost $1.25 each. What is the least she has to spend to get the rope she needs?"""
    inches_needed = 10 * 6
    feet_needed = inches_needed / 12
    six_foot_rope_cost = 5
    one_foot_rope_cost = 1.25
    total_cost_six_foot_rope = six_foot_rope_cost
    total_cost_one_foot_rope = feet_needed * one_foot_rope_cost
    if total_cost_one_foot_rope < total_cost_six_foot_rope:
        result = total_cost_one_foot_rope
    else:
        result = total_cost_six_foot_rope

    return result

print(solution())