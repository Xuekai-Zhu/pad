def solution():
    """Shara had 20 shells before she went on vacation. On vacation, she found 5 shells per day for 3 days. Then she found 6 shells on the fourth day. How many shells does she have now?"""
    starting_shells = 20
    shells_found = 5 * 3 + 6
    total_shells = starting_shells + shells_found
    result = total_shells
    return result

print(solution())