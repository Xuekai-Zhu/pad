def solution():
    # Let's assume Sara's height to be x
    # Joe's height is 6 inches more than double Sara's height, so Joe's height is 2x + 6

    # Combined height of Sara and Joe is 120 inches
    # Therefore, x + (2x + 6) = 120

    # Solving the equation for x gives us Sara's height
    sara_height = (120 - 6) / 3  # Subtracting 6 from 120 and dividing by 3

    # Joe's height is 6 inches more than double Sara's height
    joe_height = 2 * sara_height + 6

    result = joe_height
    return result

print(solution())