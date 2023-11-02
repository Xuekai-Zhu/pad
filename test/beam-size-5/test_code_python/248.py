def solution():
    
    last_night_wolves = 10
    last_night_cougars = 15
    today_wolves = 3 * last_night_wolves
    today_cougars = last_night_cougars - 3
    total_wolves = last_night_wolves + last_night_cougars
    total_cougars = last_night_cougars + today_wolves
    total_animals = total_wolves + total_cougars
    result = total_animals
    return result

print(solution())