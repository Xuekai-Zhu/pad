def solution():
    # Adjust the count for the double-counted and missed toddlers
    actual_count = 26 - 8/2 + 3  # double-counted toddlers count as half, missed toddlers need to be added
    result = actual_count
    return result

print(solution())