def solution():
    
    sh_dog_time = 10 
    fh_dog_time = 2 * sh_dog_time 
    total_time = (sh_dog_time * 6) + (fh_dog_time * 9) 
    total_time_in_hours = total_time / 60 
    result = total_time_in_hours
    return result

print(solution())