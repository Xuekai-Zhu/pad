def solution():
    
    # Define the total number of people in the Fine Arts Center
    total_people = 6000

    # Calculate the number of seats for graduates and faculty attending
    graduate_seats = 950
    faculty_attending_seats = 300

    # Calculate the total number of seats for graduates and faculty attending
    total_graduate_and_faculty_attending_seats = graduate_seats + faculty_attending_seats

    # Calculate the number of tickets each graduate would receive if they split equally
    tickets_per_graduate = total_graduate_and_faculty_attending_seats / total_people

    # Display the number of tickets each graduate would receive
    result = tickets_per_graduate
    return result

print(solution())