def solution():
    """For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. 
    If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?"""
    cans_recycled = 144
    newspapers_recycled = 20
    can_reward = 0.5
    newspaper_reward = 1.5
    total_reward = (cans_recycled // 12) * can_reward + (newspapers_recycled // 5) * newspaper_reward
    result = round(total_reward, 2)
    return result

print(solution())