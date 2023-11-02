def solution():
    """John takes 3 naps a week. Each nap is 2 hours long. In 70 days how many hours of naps does he take?"""
    # Calculate the number of naps John takes in 70 days
    naps = (70 / 7) * 3

    # Calculate the total number of hours John spends napping
    total_hours = naps * 2

    # Return the result
    result = total_hours
    return result

print(solution())