def solution():
    """The number of coronavirus cases in a certain country was 300 infections per day during the first wave. However, the number of cases increased by four times more per day as a new coronavirus variant started infecting people in a second wave. What was the total number of infections during the second wave in 2 weeks?"""
    # Define the number of infections per day during the first wave
    first_wave_cases = 300

    # Define the increase in infections per day for the second wave
    increase_factor = 4

    # Define the number of weeks in the second wave
    second_wave_weeks = 2

    # Calculate the number of infections per day during the second wave
    second_wave_cases = first_wave_cases * increase_factor

    # Calculate the total number of infections during the second wave
    total_cases = second_wave_cases * 7 * second_wave_weeks

    # Display the total number of infections
    result = total_cases
    return result

print(solution())