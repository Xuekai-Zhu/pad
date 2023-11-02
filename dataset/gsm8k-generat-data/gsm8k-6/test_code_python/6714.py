def solution():
    # Set the initial reward amounts for each grade
    b_plus_reward = 5 
    a_reward = 10 

    # Calculate the maximum amount Paul can receive
    total_courses = 10  # number of courses in Paul's scorecard
    max_a_plus = 2  # minimum number of A+ required to double previous rewards
    a_plus_count = 0  # count of A+ grades obtained
    total_reward = 0  # total reward amount

    for i in range(total_courses):
        grade = input()  # obtain the grade for each course
        if grade == "A+":
            a_plus_count += 1
            if a_plus_count >= max_a_plus:
                total_reward += 15
            else:
                total_reward += a_reward
        elif grade == "A":
            total_reward += a_reward
        elif grade == "B+":
            total_reward += b_plus_reward

    result = total_reward
    return result

print(solution())