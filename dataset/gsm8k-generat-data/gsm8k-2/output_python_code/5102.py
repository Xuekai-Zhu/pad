def solution():
    """During the hot dog eating contest, the 1st competitor ate 12 hot dogs in 3 minutes. The 2nd competitor ate twice that amount and the 3rd competitor ate 25% less than the 2nd competitor. How many hotdogs did the 3rd competitor eat?"""
    competitor1_hotdogs = 12
    competitor2_hotdogs = competitor1_hotdogs * 2
    competitor3_hotdogs = competitor2_hotdogs * 0.75
    result = competitor3_hotdogs
    return result

print(solution())