def solution():
    num_courses = 10  # There are 10 courses in Paul's scorecard
    b_plus_reward = 5  # Paul gets $5 for every B+
    a_reward = 10  # Paul gets $10 for every A (twice the reward for a B+)
    a_plus_reward = 15  # Paul gets $15 for every A+ (with no extra bonus for A+)

    # Calculate the maximum reward Paul can receive for B+ and A grades
    max_b_plus_reward = b_plus_reward * num_courses
    max_a_reward = a_reward * num_courses

    # Calculate the maximum reward Paul can receive for A+ grades
    num_a_plus = 2  # Paul needs to get at least two A+ to double the rewards
    max_a_plus_reward = a_plus_reward * num_a_plus

    # Add up the maximum rewards for all grades
    total_reward = max_b_plus_reward + max_a_reward + max_a_plus_reward
    result = total_reward
    return result

print(solution())