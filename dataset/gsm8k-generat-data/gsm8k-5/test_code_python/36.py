def solution():
    total_earned = 60  # The three of them earned $60 in total
    lisa_earned = total_earned / 2  # Lisa earned half of the total
    tommy_earned = lisa_earned / 2  # Tommy earned half of what Lisa earned

    # Calculate the difference in earnings between Lisa and Tommy
    difference = lisa_earned - tommy_earned
    result = difference
    return result

print(solution())