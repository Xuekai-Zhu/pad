def solution():
    total_pistachios = 80  # The bag has 80 pistachios
    pistachios_with_shells = 0.95 * total_pistachios  # 95% of the pistachios have shells
    pistachios_with_opened_shells = 0.75 * pistachios_with_shells  # 75% of those with shells have opened shells

    # Calculate the total number of pistachios with shells and opened shells
    pistachios_with_opened_and_closed_shells = pistachios_with_shells * pistachios_with_opened_shells
    result = pistachios_with_opened_and_closed_shells
    return result

print(solution())