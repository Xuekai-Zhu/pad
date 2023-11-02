def solution():
    """In a hotdog eating competition, the first competitor can eat 10 hot dogs per minute. The second competitor can eat 3 times more than the first competitor, while the third competitor can eat twice as much as the second competitor. How many hotdogs can the third competitor eat after 5 minutes?"""
    competitor1_rate = 10
    competitor2_rate = 3 * competitor1_rate
    competitor3_rate = 2 * competitor2_rate
    total_hotdogs = 5 * competitor3_rate
    result = total_hotdogs
    return result

print(solution())