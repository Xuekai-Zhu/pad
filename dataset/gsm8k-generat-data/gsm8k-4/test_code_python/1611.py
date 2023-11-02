def solution():
    """Mr. and Mrs. Hugo went on a road trip. On the first day, they traveled 200 miles. 
    On the second day, they traveled 3/4 as far. On the third day, they traveled 1/2 as many miles as 
    the first two days combined. How many miles did they travel for 3 days?"""
    
    # Calculate the distance traveled on the second day
    second_day_distance = 200 * 3/4
    
    # Calculate the total distance traveled on the first two days
    first_two_days_distance = 200 + second_day_distance
    
    # Calculate the distance traveled on the third day
    third_day_distance = first_two_days_distance * 1/2
    
    # Calculate the total distance traveled in 3 days
    total_distance = 200 + second_day_distance + third_day_distance
    
    result = total_distance
    return result

print(solution())