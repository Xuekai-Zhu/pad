def solution():
    """Candace is trying to decide whether to wear her old shoes or new high-tech shoes for a hike. The high-tech shoes will help Candace walk twice as fast, but they're not broken in yet, so she'll get 1 blister after every 2 hours she spends walking in them. Each blister slows Candance down by 2 miles per hour. If Candace walks 6 miles per hour in the old shoes and plans to hike for 4 hours, how many miles per hour can she go in the new shoes?"""
    # Define Candace's old walking speed and hiking time
    old_speed = 6
    hiking_time = 4

    # Define the walking speed and blister rate for the new shoes
    new_speed = 2 * old_speed
    blister_rate = 1 / 2

    # Calculate the number of blisters Candace will get
    num_blisters = hiking_time // 2

    # Calculate how much the blisters will slow Candace down
    speed_loss = num_blisters * 2

    # Calculate Candace's new walking speed
    new_speed = new_speed - speed_loss

    # Display Candace's new walking speed
    result = new_speed
    return result

print(solution())