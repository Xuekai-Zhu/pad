def solution():
    """Paul's grades last semester were very bad. To encourage him, Paul's dad promised him $5 for every B+ he gets in his next scorecard and twice that amount for every A. If Paul obtains at least two A+ he'll double the previous rewards and would receive a flat $15 for every A+ obtained (with no extra bonus). If there are 10 courses with grades in Paul's scorecard, what's the maximum amount he could receive from his dad?"""
    
    num_courses = 10
    bplus_reward = 5
    a_reward = 2 * bplus_reward
    double_a_reward = 15
    aplus_count = 0
    total_reward = 0
    
    for i in range(num_courses):
        grade = input("Enter grade: ").upper() # Assuming user enters grade in A, B+, B, etc. format
        if grade == "A+":
            aplus_count += 1
            total_reward += double_a_reward
        elif grade == "A":
            total_reward += a_reward
        elif grade == "B+":
            total_reward += bplus_reward
    
    # If Paul obtained at least two A+, double all rewards for A and B+
    if aplus_count >= 2:
        total_reward += (2 * a_reward) + (2 * bplus_reward)
    
    return total_reward

print(solution())