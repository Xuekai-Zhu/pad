def solution():
    """Candace is trying to decide whether to wear her old shoes or new high-tech shoes for a hike. The high-tech shoes will help Candace walk twice as fast, but they're not broken in yet, so she'll get 1 blister after every 2 hours she spends walking in them.
    Each blister slows Candance down by 2 miles per hour. If Candance walks 6 miles per hour in the old shoes and plans to hike for 4 hours, how many miles per hour can she go in the new shoes?"""
    # Define Candace's walking speed in her old shoes
    old_shoes_speed = 6  # miles per hour

    # Define the duration of the hike
    hike_duration = 4  # hours

    # Define the walking speed reduction due to each blister
    blister_speed_reduction = 2  # miles per hour

    # Define the intervals at which Candace gets blisters
    blister_interval = 2  # hours

    # Define the walking speed in the new shoes
    new_shoes_speed = old_shoes_speed * 2

    # Calculate the number of blisters Candace will get on the hike
    num_blisters = hike_duration // blister_interval

    # Calculate the speed reduction due to the blisters
    speed_reduction = num_blisters * blister_speed_reduction

    # Calculate the final walking speed in the new shoes
    final_speed = new_shoes_speed - speed_reduction

    # Return the result
    result = final_speed
    return result

print(solution())