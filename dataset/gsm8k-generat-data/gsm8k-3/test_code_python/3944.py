def solution():
    """Sara and Joe have a combined height of 120 inches. Joe is 6 inches more than double Sara's height. How tall is Joe?"""
    # Define Sara's height as "s"
    s = x

    # Calculate Joe's height in terms of s
    j = (2*s) + 6

    # Calculate the total height of Sara and Joe
    total_height = s + j

    # Use the given fact that their total height is 120 inches to solve for s
    s = (120 - 6) / 3

    # Calculate Joe's height using the value of s just found
    j = (2 * s) + 6

    # Display Joe's height
    result = j
    return result

print(solution())