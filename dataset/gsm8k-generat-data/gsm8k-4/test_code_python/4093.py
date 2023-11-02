def solution():
    """A judge oversaw seventeen court cases. Two were immediately dismissed from court. Two-thirds of the remaining cases were ruled innocent, one ruling was delayed until a later date, and the rest were judged guilty. On how many cases did the judge rule guilty?"""
    # Define the initial number of court cases
    total_cases = 17

    # Define the number of cases that were immediately dismissed
    dismissed_cases = 2

    # Calculate the number of remaining cases
    remaining_cases = total_cases - dismissed_cases

    # Calculate the number of cases ruled innocent
    innocent_cases = remaining_cases * 2/3

    # Calculate the number of cases ruled guilty
    guilty_cases = remaining_cases - innocent_cases - 1

    # Return the result
    result = guilty_cases
    return result

print(solution())