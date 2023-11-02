def solution():
    """Andy can get 50 demerits in a month before getting fired. If he got 2 demerits per instance for showing up late 6 times and 15 demerits for making an inappropriate joke, how many more demerits can he get this month before getting fired?"""
    # Define the demerit limits and the demerits that Andy has already received
    DEMERIT_LIMIT = 50
    CURRENT_DEMERITS = 6 * 2 + 15

    # Calculate the remaining demerit limit
    remaining_limit = DEMERIT_LIMIT - CURRENT_DEMERITS

    # Return the result
    result = remaining_limit
    return result

print(solution())