def solution():
    """There were 90 people at the summer picnic. There were 50 soda cans, 50 plastic bottles of sparkling water, and 50 glass bottles of juice. One-half of the guests drank soda, one-third of the guests drank sparkling water, and four-fifths of the juices were consumed. How many recyclable cans and bottles were collected?"""
    total_guests = 90
    soda_cans = 50
    sparkling_water_bottles = 50
    juice_bottles = 50
    soda_consumers = total_guests / 2
    sparkling_water_consumers = total_guests / 3
    juice_consumers = total_guests
    total_soda_cans = soda_consumers * 1
    total_sparkling_water_bottles = sparkling_water_consumers * 1
    total_juice_bottles = juice_bottles * 0.2
    total_recyclables = total_soda_cans + total_sparkling_water_bottles + total_juice_bottles
    result = total_recyclables
    return result

print(solution())