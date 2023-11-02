def solution():
    """A man loves to go hiking. He knows that he has to pack about .5 pounds of supplies for every mile he hikes. He plans to go for a very long hike. He knows that he can get 1 resupply during the hike that will be 25% as large as his first pack. He can hike at a rate of 2.5 mph. He is going to hike 8 hours a day for 5 days. How much does he need to bring with his first pack?"""
    miles_per_day = 2.5 * 8
    total_miles = miles_per_day * 5
    supplies_per_mile = 0.5
    total_supplies = supplies_per_mile * total_miles
    resupply_ratio = 0.25
    resupply_supplies = total_supplies * resupply_ratio
    first_pack_supplies = total_supplies - resupply_supplies
    result = first_pack_supplies
    return result

print(solution())