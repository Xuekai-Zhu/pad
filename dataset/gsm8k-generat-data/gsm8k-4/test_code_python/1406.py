def solution():
    """Bill is trying to count the toddlers at his daycare, but they keep running around. He double-counts 8 toddlers and misses 3 who are hiding. If Bill thinks he counted 26 toddlers, how many are there really?"""
    # Define the number of toddlers Bill counted
    counted_toddlers = 26

    # Calculate the actual number of toddlers
    actual_toddlers = counted_toddlers - 8 + 3

    # Return the result
    result = actual_toddlers
    return result

print(solution())