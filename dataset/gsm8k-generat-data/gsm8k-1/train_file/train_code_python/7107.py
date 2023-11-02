def solution():
    """As a child, Bobby was able to jump rope 30 times per minute. Now that he is an adult, he can jump 1 jump per second. How many more jumps than when he was a child is Bobby able to jump now that he is an adult?"""
    child_jumps_per_minute = 30
    adult_jumps_per_minute = 60
    adult_jumps_per_second = 1
    child_jumps_total = child_jumps_per_minute * 10  # Assuming he jumps for 10 minutes
    adult_jumps_total = adult_jumps_per_minute * 10 * adult_jumps_per_second # Assuming he jumps for 10 minutes
    difference = adult_jumps_total - child_jumps_total
    result = difference
    return result

print(solution())