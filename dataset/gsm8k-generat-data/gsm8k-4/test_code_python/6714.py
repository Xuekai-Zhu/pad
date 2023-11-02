def solution():
    """Paul's grades last semester were very bad. To encourage him, Paul's dad promised him $5 for every B+ he gets in his next scorecard and twice that amount for every A. If Paul obtains at least two A+ he'll double the previous rewards and would receive a flat $15 for every A+ obtained (with no extra bonus). If there are 10 courses with grades in Paul's scorecard, what's the maximum amount he could receive from his dad?"""
    # Define the reward for a B+ and an A
    BPLUS_REWARD = 5
    A_REWARD = 10
    
    # Define the reward for an A+ and the number required for the bonus
    APLUS_REWARD = 15
    APLUS_BONUS = 2

    # Define the number of courses and initialize the counters for each grade
    NUM_COURSES = 10
    bplus_count = 0
    a_count = 0
    aplus_count = 0

    # Prompt user for inputting the grades of each course
    for i in range(NUM_COURSES):
        grade = input("Enter the grade for course {}: ".format(i+1))
        if grade == "B+":
            bplus_count += 1
        elif grade == "A":
            a_count += 1
        elif grade == "A+":
            aplus_count += 1
    
    # Calculate the total reward for B+ and A grades
    total_bplus_reward = bplus_count * BPLUS_REWARD
    total_a_reward = a_count * A_REWARD
    
    # Check if bonus for A+ grades is applicable
    if aplus_count >= APLUS_BONUS:
        total_aplus_reward = aplus_count * APLUS_REWARD
    else:
        total_aplus_reward = aplus_count * A_REWARD * 2
    
    # Calculate the maximum reward possible
    max_reward = total_bplus_reward + total_a_reward + total_aplus_reward
    
    result = max_reward
    return result

print(solution())