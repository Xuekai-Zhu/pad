def solution():
    """A judge oversaw seventeen court cases. Two were immediately dismissed from court. Two-thirds of the remaining cases were ruled innocent, one ruling was delayed until a later date, and the rest were judged guilty. On how many cases did the judge rule guilty?"""
    total_cases = 17
    dismissed_cases = 2
    remaining_cases = total_cases - dismissed_cases
    innocent_cases = (2/3) * remaining_cases
    delayed_cases = 1
    guilty_cases = remaining_cases - innocent_cases - delayed_cases
    result = guilty_cases
    return result

print(solution())