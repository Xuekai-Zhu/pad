def solution():
    # Define Emily's credits
    emily_credits = 20

    # Calculate Spencer's credits
    spencer_credits = emily_credits / 2

    # Calculate Aria's credits
    aria_credits = spencer_credits * 2

    # Calculate the total credits
    total_credits = emily_credits + spencer_credits + aria_credits

    # Calculate twice the total credits
    twice_total_credits = 2 * total_credits

    result = twice_total_credits
    return result

print(solution())