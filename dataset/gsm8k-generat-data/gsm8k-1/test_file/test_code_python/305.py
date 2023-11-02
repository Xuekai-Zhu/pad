def solution():
    """Helena is a mad scientist testing her latest creation, the Lots-of-Limbs Serum. The serum will make the drinker grow an extra arm every three days and an extra leg every five days. After fifteen days, how many new limbs will Helena’s serum cause a person to grow if they drink it?"""
    arms_per_day = 1/3
    legs_per_day = 1/5
    days = 15
    total_arms = days * arms_per_day
    total_legs = days * legs_per_day
    new_arms = total_arms - (total_arms//1)
    new_legs = total_legs - (total_legs//1)
    result = (int(new_arms * 10) + int(new_legs * 10))/10
    return result

print(solution())