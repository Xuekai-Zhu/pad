def solution():
    feet_needed = 10
    inches_needed = feet_needed * 12
    ropes_needed = inches_needed / 6
    cost_of_6_foot_rope = 5
    cost_of_1_foot_rope = 1.25
    six_foot_rope_lengths_needed = math.ceil(ropes_needed / 6)
    one_foot_rope_lengths_needed = ropes_needed - (6 * six_foot_rope_lengths_needed)
    cost = (six_foot_rope_lengths_needed * cost_of_6_foot_rope) + (one_foot_rope_lengths_needed * cost_of_1_foot_rope)
    result = cost
    return result

print(solution())