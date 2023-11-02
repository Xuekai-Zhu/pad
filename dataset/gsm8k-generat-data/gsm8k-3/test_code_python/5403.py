def solution():
    """Brody’s calculator can run for 60 hours on a full battery. Brody has used three quarters of its battery up, and he is about to take a two-hour math exam that will require his calculator the whole time. How many hours of battery will Brody’s calculator have left?"""
    # Define the total battery life of the calculator
    TOTAL_BATTERY_LIFE = 60

    # Calculate the remaining battery life before the math exam
    remaining_battery_life = TOTAL_BATTERY_LIFE * 0.25

    # Calculate the remaining battery life after the math exam
    remaining_battery_life -= 2

    # Display the remaining battery life
    result = remaining_battery_life
    return result

print(solution())