def solution():
    initial_cutting_rate = 10  # The Albaszu machine was cutting 10 trees daily initially
    productivity_increase_ratio = 1.5  # The productivity increased by 1.5 times after the machine was repaired

    # Calculate the current cutting rate of the Albaszu machine
    current_cutting_rate = initial_cutting_rate * productivity_increase_ratio
    result = current_cutting_rate
    return result

print(solution())