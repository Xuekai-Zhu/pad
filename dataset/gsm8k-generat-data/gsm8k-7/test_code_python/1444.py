def solution():
    emily_credits = 20
    spencer_credits = emily_credits / 2
    aria_credits = 2 * emily_credits

    # Calculate the total number of credits the three have
    total_credits = emily_credits + spencer_credits + aria_credits

    # Calculate twice the total number of credits
    result = 2 * total_credits
    return result

print(solution())