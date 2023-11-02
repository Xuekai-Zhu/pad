def solution():
    """Markese earned 5 fewer dollars than Evan. Together they earned $37. How many dollars did Markese earn? Use E to represent how many dollars Evan earned."""
    total_earned = 37
    evan_earned = (total_earned + 5) / 2
    markese_earned = evan_earned - 5
    result = markese_earned
    return result

print(solution())