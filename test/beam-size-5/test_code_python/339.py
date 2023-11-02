def solution():
    
    # Define the number of days in June
    days_in_june = 30

    # Define the number of meters Tyson runs per day
    tyson_distance = 5000

    # Calculate the number of meters Tyson wants the coach to run in a day
    coach_distance = tyson_distance * (1 + 1/5)

    # Calculate the total distance covered in June
    total_distance = tyson_distance * days_in_june

    # Display the total distance covered
    result = total_distance
    return result

print(solution())