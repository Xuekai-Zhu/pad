def solution():
    """Paul's grades last semester were very bad. To encourage him, Paul's dad promised him $5 for every B+ he gets in his next scorecard and twice that amount for every A. If Paul obtains at least two A+ he'll double the previous rewards and would receive a flat $15 for every A+ obtained (with no extra bonus). If there are 10 courses with grades in Paul's scorecard, what's the maximum amount he could receive from his dad?"""
    # Define the reward amounts for each grade
    BPLUS_REWARD = 5
    A_REWARD = 10
    APLUS_REWARD = 15

    # Initialize the number of each grade
    num_bplus = 0
    num_a = 0
    num_aplus = 0

    # Get the grades for each course
    for i in range(10):
        grade = input("Enter grade for course {}: ".format(i+1))
        if grade == "B+":
            num_bplus += 1
        elif grade == "A":
            num_a += 1
        elif grade == "A+":
            num_aplus += 1

    # Calculate the total reward amount
    total_reward = num_bplus * BPLUS_REWARD + num_a * A_REWARD + num_aplus * APLUS_REWARD
    if num_aplus >= 2:
        total_reward += num_aplus * APLUS_REWARD

    # Display the maximum reward amount
    result = total_reward
    return result

print(solution())