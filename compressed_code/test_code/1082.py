def solution():
    
    num_boys = 16
    num_girls = 14
    boy_gifts = (3/4) * num_boys
    girl_gifts = (6/7) * num_girls
    total_gifted = boy_gifts + girl_gifts
    total_attendees = num_boys + num_girls
    no_gifts = total_attendees - total_gifted
    result = no_gifts
    return result

print(solution())