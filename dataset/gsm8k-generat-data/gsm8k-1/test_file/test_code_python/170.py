def solution():
    """Billy is peeling and cutting potatoes in preparation for making potato salad for his big family reunion barbecue. It's a big event, so he has 60 potatoes to get through. The potatoes are roughly the same size, so it takes about the same amount of time to peel and cut each one. It takes Billy about a minute and a half to peel a potato, but only about 5 seconds to cut it up. How long will it take Billy to finish prepping the potatoes?"""
    num_potatoes = 60
    time_per_potato_peel = 90  # seconds
    time_per_potato_cut = 5  # seconds
    total_time = (num_potatoes * time_per_potato_peel) + (num_potatoes * time_per_potato_cut)
    result = total_time
    
    return result

print(solution())