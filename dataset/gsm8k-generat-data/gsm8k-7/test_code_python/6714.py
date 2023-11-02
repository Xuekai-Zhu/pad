def solution():
    num_courses = 10
    bplus_reward = 5
    a_reward = 2 * bplus_reward
    aplus_reward = 15
    num_aplus_needed = 2

    # Initialize counters for each grade level
    num_bplus = 0
    num_a = 0
    num_aplus = 0

    # Simulate Paul's grades randomly
    for i in range(num_courses):
        grade = random.randint(1, 100)
        if grade >= 90:
            num_aplus += 1
        elif grade >= 80:
            num_a += 1
        elif grade >= 70:
            num_bplus += 1

    # Calculate total reward
    total_reward = num_bplus * bplus_reward + num_a * a_reward

    if num_aplus >= num_aplus_needed:
        total_reward += num_aplus_needed * aplus_reward
        total_reward *= 2
        total_reward += (num_aplus - num_aplus_needed) * a_reward

    result = total_reward
    return result

print(solution())