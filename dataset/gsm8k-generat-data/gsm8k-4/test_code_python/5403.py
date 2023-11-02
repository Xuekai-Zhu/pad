def solution():
    """Brody’s calculator can run for 60 hours on a full battery. Brody has used three quarters of its battery up, and he is about to take a two-hour math exam that will require his calculator the whole time. How many hours of battery will Brody’s calculator have left?"""
    # Define the total battery life and calculate the remaining battery life
    total_battery = 60
    remaining_battery = total_battery * (1 - 0.75)

    # Calculate the battery life remaining after the math exam
    remaining_battery -= 2

    # Return the result
    result = remaining_battery
    return result

print(solution())