def solution():
    """Tanesha needs to buy rope so cut into 10 pieces that are each six inches long. 
    She sees a 6-foot length of rope that cost $5 and also sees 1-foot lengths of rope 
    that cost $1.25 each. What is the least she has to spend to get the rope she needs?"""
    # Define the length of rope Tanesha needs in inches
    rope_length = 10 * 6

    # Calculate the cost of the 6-foot rope
    six_foot_cost = 5

    # Calculate the cost of the 1-foot rope
    one_foot_cost = 1.25

    # Calculate the number of 1-foot ropes Tanesha needs
    num_one_foot = rope_length / 12

    # Calculate the total cost of buying only 1-foot ropes
    one_foot_total_cost = num_one_foot * one_foot_cost

    # Calculate the total cost of buying one 6-foot rope and any remaining length in 1-foot ropes
    six_foot_total_cost = six_foot_cost + one_foot_cost * (num_one_foot % 6)

    # Determine which option is cheaper and return that cost
    if one_foot_total_cost < six_foot_total_cost:
        result = one_foot_total_cost
    else:
        result = six_foot_total_cost
    return result

print(solution())