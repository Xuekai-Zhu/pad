def solution():
    """New York recorded 5000 new coronavirus cases on a particular week. In the second week, half as many new coronaviruses cases as the first week was recorded by the state. In the third week, 2000 more cases were recorded in the state. What is the total number of recorded new coronaviruses in the state after the three weeks?"""
    # Define the number of new coronavirus cases in the first week
    cases_1 = 5000

    # Calculate the number of new coronavirus cases in the second week
    cases_2 = cases_1 / 2

    # Calculate the number of new coronavirus cases in the third week
    cases_3 = cases_2 + 2000

    # Calculate the total number of new coronavirus cases over the three weeks
    total_cases = cases_1 + cases_2 + cases_3

    # Display the total number of new coronavirus cases
    result = total_cases
    return result

print(solution())