def solution():
    num_dogs = 2
    groom_time_per_dog = 20 # in minutes
    num_days = 30
    
    # Calculate the total grooming time for both dogs in one day
    total_groom_time_per_day = num_dogs * groom_time_per_dog
    
    # Calculate the total grooming time for both dogs in 30 days
    total_groom_time = total_groom_time_per_day * num_days
    
    # Convert grooming time from minutes to hours
    total_groom_time_hours = total_groom_time / 60
    
    result = total_groom_time_hours
    return result

print(solution())