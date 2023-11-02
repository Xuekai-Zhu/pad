def solution():
    """It was reported that 2000 cases of Coronavirus had been confirmed in the state of New York in May 2020. There was half the number of cases in California, which had 400 more cases than the state of Texas. What's the total number of cases that had been confirmed in all of these states?"""
    # Define the number of cases in New York
    NY_CASES = 2000

    # Calculate the number of cases in California
    CA_CASES = NY_CASES / 2

    # Calculate the number of cases in Texas
    TX_CASES = CA_CASES - 400

    # Calculate the total number of cases in all three states
    total_cases = NY_CASES + CA_CASES + TX_CASES

    # Display the total number of cases
    result = total_cases
    return result

print(solution())