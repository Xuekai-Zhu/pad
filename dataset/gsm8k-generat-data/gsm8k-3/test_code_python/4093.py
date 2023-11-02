def solution():
    """A judge oversaw seventeen court cases. Two were immediately dismissed from court. Two-thirds of the remaining cases were ruled innocent, one ruling was delayed until a later date, and the rest were judged guilty. On how many cases did the judge rule guilty?"""
    # Define the number of cases dismissed and the total number of cases
    cases_dismissed = 2
    total_cases = 17

    # Calculate the number of cases remaining after dismissal
    cases_after_dismissal = total_cases - cases_dismissed

    # Calculate the number of cases ruled innocent
    cases_innocent = (2/3) * cases_after_dismissal

    # Calculate the number of cases delayed for ruling
    cases_delayed = 1

    # Calculate the number of cases ruled guilty
    cases_guilty = cases_after_dismissal - cases_innocent - cases_delayed

    # Display the number of cases ruled guilty
    result = cases_guilty
    return result

print(solution())