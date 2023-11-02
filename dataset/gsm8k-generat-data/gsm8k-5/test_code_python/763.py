def solution():
    total_ribbon = 18  # Josh has 18 yards of ribbon
    gifts = 6  # There are 6 gifts that need to be wrapped equally

    # Calculate the total amount of ribbon used by all the gifts
    ribbon_used = gifts * 2

    # Calculate the amount of ribbon left
    ribbon_left = total_ribbon - ribbon_used
    result = ribbon_left
    return result

print(solution())