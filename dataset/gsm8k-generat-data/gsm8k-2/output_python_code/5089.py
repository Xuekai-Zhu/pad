def solution():
    """Mark is running for an election and wins 70% of the votes in an area with 100,000 voters. He got twice as many total votes in the remaining area. How many votes did he get in total?"""
    area_voters = 100000
    mark_votes = 0.7 * area_voters
    remaining_votes = 2 * (1 - 0.7) * area_voters
    total_votes = mark_votes + remaining_votes
    result = total_votes
    return result

print(solution())