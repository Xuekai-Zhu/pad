def solution():
    
    # Define the distance Tyson runs each day and the coach wants to run 1/5 times more meters
    daily_distance = 5000
    coach_additional_distance = daily_distance * (1 + 1/5)

    # Calculate the total distance Tyson covered in a month
    total_distance = daily_distance * 30 + coach_additional_distance * 30

    # Display the total distance covered in June
    result = total_distance
    return result

print(solution())