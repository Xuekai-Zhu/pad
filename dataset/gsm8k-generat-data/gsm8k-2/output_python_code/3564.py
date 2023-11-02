def solution():
    """Everett built a rectangular concrete patio that was four times as long as it was wide. If the perimeter of the patio was 100 feet, what was the length of the patio, in feet?"""
    # Let's call the width "w"
    w = 100 / (2 + 4)
    # The length is four times the width
    l = 4 * w
    result = l
    return result

print(solution())