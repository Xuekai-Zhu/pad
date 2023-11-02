def solution():
    # Calculate the number of pistachios with shells
    pistachios_with_shells = 0.95 * 80

    # Calculate the number of pistachios with both shells and opened shells
    pistachios_with_opened_shells = 0.75 * pistachios_with_shells

    result = pistachios_with_opened_shells
    return result

print(solution())