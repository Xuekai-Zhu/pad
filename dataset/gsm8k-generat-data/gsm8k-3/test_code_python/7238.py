def solution():
    """A man loves to go hiking.  He knows that he has to pack about .5 pounds of supplies for every mile he hikes.  He plans to go for a very long hike.  He knows that he can get 1 resupply during the hike that will be 25% as large as his first pack.  He can hike at a rate of 2.5 mph.  He is going to hike 8 hours a day for 5 days.  How much does he need to bring with his first pack?"""
    
    # Define constants
    SUPPLIES_PER_MILE = 0.5

    # Calculate distance hiked each day
    daily_distance = 2.5 * 8

    # Calculate total distance hiked
    total_distance = daily_distance * 5

    # Calculate amount of supplies needed for entire hike
    total_supplies = total_distance * SUPPLIES_PER_MILE

    # Calculate amount of supplies for first pack
    first_pack = total_supplies / 1.25

    result = first_pack
    return result

print(solution())