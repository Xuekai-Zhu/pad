def solution():
    """In a hotdog eating competition, the first competitor can eat 10 hot dogs per minute. The second competitor can eat 3 times more than the first competitor, while the third competitor can eat twice as much as the second competitor. How many hotdogs can the third competitor eat after 5 minutes?"""
    competitor1 = 10
    competitor2 = competitor1 * 3
    competitor3 = competitor2 * 2
    minutes = 5
    hotdogs_eaten = competitor3 * minutes
    result = hotdogs_eaten
    return result

print(solution())