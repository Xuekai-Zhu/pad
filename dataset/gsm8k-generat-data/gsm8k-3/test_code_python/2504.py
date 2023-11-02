def solution():
    """Elsie has a specific amount of wet wipes in a container in the morning. Throughout the day, she refills the container with 10 more wipes after using up 20. By nighttime, she only has 60 wipes left. How many wipes were in the container in the morning?"""
    # Define the amount of wipes used and added throughout the day
    used_wipes = 20
    added_wipes = 10

    # Define the number of wipes left at night
    remaining_wipes = 60

    # Calculate the total number of times Elsie refilled the container
    num_refills = (remaining_wipes - used_wipes) / (added_wipes - used_wipes)

    # Calculate the number of wipes in the container in the morning
    morning_wipes = remaining_wipes - num_refills * added_wipes

    # Display the number of wipes in the container in the morning
    result = morning_wipes
    return result

print(solution())