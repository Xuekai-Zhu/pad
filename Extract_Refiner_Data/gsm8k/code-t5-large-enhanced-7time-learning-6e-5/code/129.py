def solution():
    
    # Define the number of miles Walt walked on Monday
    monday_miles = 4

    # Calculate the number of miles Walt walked on Tuesday
    tuesday_miles = monday_miles * 6

    # Calculate the total miles Walt walked on Monday through Wednesday
    total_miles = 41

    # Calculate the number of miles Walt walked on Wednesday
    wednesday_miles = total_miles - monday_miles - tuesday_miles

    # Display the number of miles Walt walked on Wednesday
    result = wednesday_miles
    return result

print(solution())