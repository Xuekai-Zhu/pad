def solution():
    """Everett built a rectangular concrete patio that was four times as long as it was wide.  If the perimeter of the patio was 100 feet, what was the length of the patio, in feet?"""
    # Let's assume the width of the patio to be x
    x = 100 / (2 + 4)
    length = 4 * x

    result = length
    return result

print(solution())