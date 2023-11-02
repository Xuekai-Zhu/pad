def solution():
    # Define variables
    num_courses = 10
    b_plus_reward = 5
    a_plus_reward = 10
    a_plus_double_reward = 15
    num_a_plus = 0
    total_reward = 0

    # Loop through each course and check the grade
    for i in range(num_courses):
        grade = input("Enter grade for course " + str(i+1) + ": ")
        if grade == "A+":
            total_reward += a_plus_reward
            num_a_plus += 1
        elif grade == "B+":
            total_reward += b_plus_reward
    
    # Check if Paul gets double reward for A+ grades
    if num_a_plus >= 2:
        total_reward += (num_a_plus - 1) * a_plus_double_reward
        total_reward += 15 * num_a_plus
    
    result = total_reward
    return result

print(solution())