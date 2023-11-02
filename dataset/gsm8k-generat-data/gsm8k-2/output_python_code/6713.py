def solution():
    """Paul's grades last semester were very bad. To encourage him, Paul's dad promised him $5 for every B+ he gets in his next scorecard and twice that amount for every A. If Paul obtains at least two A+ he'll double the previous rewards and would receive a flat $15 for every A+ obtained (with no extra bonus). If there are 10 courses with grades in Paul's scorecard, what's the maximum amount he could receive from his dad?"""
    num_courses = 10
    bplus_reward = 5
    a_reward = 2 * bplus_reward
    double_a_reward = 15
    num_a = 0
    total_rewards = 0
    for i in range(num_courses):
        grade = input(f"What was your grade for course {i+1}? ")
        if grade == "A+":
            num_a += 1
            if num_a >= 2:
                total_rewards += double_a_reward
            else:
                total_rewards += a_reward
        elif grade == "A":
            num_a += 1
            total_rewards += a_reward
        elif grade == "B+":
            total_rewards += bplus_reward

    result = total_rewards
    return result

print(solution())