def solution():
    
    num_people_start = 600
    num_girls_start = 240
    num_boys_start = num_people_start - num_girls_start
    num_boys_left = num_boys_start / 4
    num_girls_left = num_girls_start / 8
    num_people_left = num_boys_left + num_girls_left
    num_people_end = num_people_start - num_people_left
    result = num_people_end
    return result

print(solution())