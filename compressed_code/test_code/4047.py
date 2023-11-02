def solution():
    
    cans_recycled = 144
    newspapers_recycled = 20
    can_reward = 0.5
    newspaper_reward = 1.5
    total_reward = (cans_recycled // 12) * can_reward + (newspapers_recycled // 5) * newspaper_reward
    result = round(total_reward, 2)
    return result

print(solution())