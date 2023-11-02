def solution():
    """Rachel drinks 2 glasses of water on Sunday and 4 glasses of water on Monday. Then she drinks 3 glasses of water every day for the next 4 days. One glass of water is 10 ounces of water. If Rachel wants to drink a total of 220 ounces of water in the week (Sunday to Saturday), how many glasses of water should she drink on Saturday?"""
    glasses = [2, 4] + [3]*4
    total_ounces = sum(glasses) * 10
    target_ounces = 220
    remaining_ounces = target_ounces - total_ounces
    saturday_glasses = remaining_ounces / 10
    result = saturday_glasses
    return result

print(solution())