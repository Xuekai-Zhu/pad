def solution():
    total_cases = 17  # The judge oversaw 17 court cases
    dismissed_cases = 2  # Two cases were immediately dismissed
    remaining_cases = total_cases - dismissed_cases  # Calculate the remaining cases
    innocent_cases = 2/3 * remaining_cases  # Two-thirds of the remaining cases were innocent
    delayed_cases = 1  # One case was delayed
    guilty_cases = remaining_cases - innocent_cases - delayed_cases  # Calculate the guilty cases

    result = guilty_cases
    return result

print(solution())