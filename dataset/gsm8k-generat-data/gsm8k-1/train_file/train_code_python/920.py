def solution():
    """There were 90 people at the summer picnic. There were 50 soda cans, 50 plastic bottles of sparkling water, and 
    50 glass bottles of juice. One-half of the guests drank soda, one-third of the guests drank sparkling water, and 
    four-fifths of the juices were consumed. How many recyclable cans and bottles were collected?"""
    num_people = 90
    num_soda_cans = 50
    num_sparkling_bottles = 50
    num_juice_bottles = 50
    
    soda_consumption = num_people/2
    sparkling_consumption = num_people/3
    juice_consumption = (4/5) * num_juice_bottles
    
    num_recyclable_cans = num_soda_cans - soda_consumption
    num_recyclable_plastic_bottles = num_sparkling_bottles - sparkling_consumption
    num_recyclable_glass_bottles = num_juice_bottles - juice_consumption
    
    total_recyclables = num_recyclable_cans + num_recyclable_plastic_bottles + num_recyclable_glass_bottles
    
    result = total_recyclables
    
    return result

print(solution())