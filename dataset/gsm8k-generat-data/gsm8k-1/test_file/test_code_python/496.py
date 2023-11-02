def solution():
    """Together Lily, David, and Bodhi collected 43 insects. Lily found 7 more than David. David found half of what Bodhi found. How many insects did Lily find?"""
    total_insects = 43
    david_insects = (total_insects-7) / 3
    bodhi_insects = david_insects * 2
    lily_insects = david_insects + 7
    result = lily_insects
    return result

print(solution())