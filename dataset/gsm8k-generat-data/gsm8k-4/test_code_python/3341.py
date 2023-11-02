def solution():
    """New York recorded 5000 new coronavirus cases on a particular week. In the second week, half as many new coronaviruses cases as the first week was recorded by the state. In the third week, 2000 more cases were recorded in the state. What is the total number of recorded new coronaviruses in the state after the three weeks?"""
    # Define the number of cases in the first week
    week1_cases = 5000

    # Calculate the number of cases in the second week
    week2_cases = week1_cases / 2

    # Calculate the number of cases in the third week
    week3_cases = week2_cases + 2000

    # Calculate the total number of cases after three weeks
    total_cases = week1_cases + week2_cases + week3_cases

    # Return the total number of cases
    result = total_cases
    return result

print(solution())