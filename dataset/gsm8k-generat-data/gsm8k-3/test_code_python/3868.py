def solution():
    """A 220-liter barrel has a small leak. It lost 10% of its contents before anyone noticed. How many liters are left in the barrel?"""
    # Define the initial volume and percentage lost
    initial_volume = 220
    percentage_lost = 0.1

    # Calculate the volume lost
    volume_lost = initial_volume * percentage_lost

    # Calculate the final volume
    final_volume = initial_volume - volume_lost

    # Display the final volume
    result = final_volume
    return result

print(solution())