def solution():
    # Define the total number of cases
    total_cases = 17

    # Subtract the two immediately dismissed cases
    remaining_cases = total_cases - 2

    # Calculate the number of innocent cases
    innocent_cases = 2/3 * remaining_cases

    # Subtract the postponed case
    remaining_cases -= 1

    # Calculate the number of guilty cases
    guilty_cases = remaining_cases - innocent_cases

    result = guilty_cases
    return result

print(solution())