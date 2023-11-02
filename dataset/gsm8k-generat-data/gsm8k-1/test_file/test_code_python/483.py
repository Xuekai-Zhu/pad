def solution():
    """Uncle Ben has four horses. Each horse can consume five pounds of oats per meal. He feeds his horses twice a day. 
    If one bag contains 50-pounds of oats, how many bags of oats does he need to fed his horses for five days?"""
    horses = 4
    oats_per_day = 5 * 2  # 5 pounds per meal and twice a day
    oats_per_week = oats_per_day * 7
    oats_per_5_days = oats_per_week / 7 * 5
    bags_per_5_days = oats_per_5_days / 50  # 1 bag contains 50 pounds
    result = bags_per_5_days
    return result

print(solution())