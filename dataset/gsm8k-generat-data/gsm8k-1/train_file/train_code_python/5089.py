def solution():
    """Mark is running for an election and wins 70% of the votes in an area with 100,000 voters. He got twice as many total votes in the remaining area. How many votes did he get in total?"""
    area_voters = 100000
    area_votes = area_voters * 0.7
    remaining_votes = area_voters - area_votes
    total_votes = area_votes + (remaining_votes * 2)
    result = total_votes
    return result

print(solution())