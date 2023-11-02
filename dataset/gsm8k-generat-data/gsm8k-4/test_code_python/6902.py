def solution():
    """Misty's favorite number is 3 times smaller than Glory's favorite number. If Glory's favorite number is 450, what's the sum of their favorite numbers?"""
    # Define Glory's favorite number
    glory_favorite = 450

    # Calculate Misty's favorite number
    misty_favorite = glory_favorite / 3

    # Calculate the sum of their favorite numbers
    favorites_sum = glory_favorite + misty_favorite

    # return the result
    result = favorites_sum
    return result

print(solution())