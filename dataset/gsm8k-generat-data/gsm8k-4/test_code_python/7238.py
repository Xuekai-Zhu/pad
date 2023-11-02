def solution():
    """A man loves to go hiking. He knows that he has to pack about .5 pounds of supplies for every mile he hikes. He plans to go for a very long hike. He knows that he can get 1 resupply during the hike that will be 25% as large as his first pack. He can hike at a rate of 2.5 mph. He is going to hike 8 hours a day for 5 days. How much does he need to bring with his first pack?"""
    # Define the rate of hiking, the number of hours per day, and the number of days
    rate = 2.5  # in miles per hour
    hours_per_day = 8
    days = 5

    # Calculate the total distance to be hiked
    total_distance = rate * hours_per_day * days

    # Calculate the total weight of supplies needed for the entire hike
    total_supplies = total_distance * 0.5

    # Calculate the weight of supplies needed for the first half of the hike
    first_half_supplies = total_supplies / 2

    # Calculate the weight of supplies needed for the resupply
    resupply_supplies = first_half_supplies * 0.25

    # Calculate the total weight of supplies needed for the first pack
    first_pack_supplies = first_half_supplies + resupply_supplies

    result = first_pack_supplies
    return result

print(solution())