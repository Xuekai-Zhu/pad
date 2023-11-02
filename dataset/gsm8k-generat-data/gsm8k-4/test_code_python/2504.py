def solution():
    """Elsie has a specific amount of wet wipes in a container in the morning. Throughout the day, she refills the container with 10 more wipes after using up 20. By nighttime, she only has 60 wipes left. How many wipes were in the container in the morning?"""
    # Define the number of wipes left at nighttime
    final_wipes = 60

    # Define the number of wipes refilled each time
    refilled_wipes = 10

    # Define the number of wipes used each time
    used_wipes = 20

    # Initialize the number of wipes in the container in the morning
    morning_wipes = None

    # Use a loop to track the number of wipes in the container throughout the day
    for _ in range(6):
        # Refill the container with 10 more wipes
        morning_wipes = final_wipes + refilled_wipes

        # Use up 20 wipes
        morning_wipes -= used_wipes

        # Update the final number of wipes left at nighttime
        final_wipes = morning_wipes

    result = morning_wipes
    return result

print(solution())