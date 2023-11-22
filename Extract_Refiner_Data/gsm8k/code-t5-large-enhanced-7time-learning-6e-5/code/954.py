def solution():
    
    # Define the number of people in the concert
    concert_audience = 48

    # Calculate the number of people Courtney had overstated by 20%
    overstated_attendance = concert_audience * 0.2

    # Calculate the number of people Courtney actually attended the concert
    actual_attendance = concert_audience - overstated_attendance

    # Display the actual number of people attended the concert
    result = actual_attendance
    return result

print(solution())