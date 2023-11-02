def solution():
    """Everett built a rectangular concrete patio that was four times as long as it was wide. If the perimeter of the patio was 100 feet, what was the length of the patio, in feet?"""
    perimeter = 100
    width = perimeter / 10  # since the perimeter is 2(l + w), we can solve for w using the formula
    length = 4 * width
    result = length
    return result

print(solution())