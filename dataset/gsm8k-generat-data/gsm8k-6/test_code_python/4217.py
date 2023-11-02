def solution():
    # Calculate the number of tourists left at the end of the tour
    remaining_tourists = (30 - 2) * 0.5 * 0.6 * (1 - (1/7))
    result = remaining_tourists
    return result

print(solution())