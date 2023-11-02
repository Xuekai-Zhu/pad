def solution():
    """Nick's cell phone was initially empty but was then charged for 45 minutes and has reached a 25% charge. How much longer must the cell phone be charged to reach 100% charge?"""
    # Define the time it took to reach a 25% charge
    initial_time = 45

    # Define the current charge percentage
    current_charge = 25

    # Define the target charge percentage
    target_charge = 100

    # Calculate the percentage increase per minute
    percentage_increase_per_minute = (target_charge - current_charge) / (60 - initial_time)

    # Calculate the time needed to reach the target charge percentage
    time_needed = (target_charge - current_charge) / percentage_increase_per_minute

    # Display the time needed
    result = time_needed
    return result

print(solution())