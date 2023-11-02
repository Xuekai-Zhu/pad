def solution():
    ny_cases = 2000
    ca_cases = ny_cases / 2
    tx_cases = ca_cases - 400

    # Calculate the total number of confirmed cases in all three states
    total_cases = ny_cases + ca_cases + tx_cases
    result = total_cases
    return result

print(solution())