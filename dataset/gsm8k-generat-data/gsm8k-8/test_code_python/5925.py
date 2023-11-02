def solution():
    # Define the number of cases in New York
    ny_cases = 2000

    # Calculate the number of cases in California
    ca_cases = ny_cases / 2

    # Calculate the number of cases in Texas
    tx_cases = ca_cases - 400

    # Calculate the total number of cases in all three states
    total_cases = ny_cases + ca_cases + tx_cases
    result = total_cases
    return result

print(solution())