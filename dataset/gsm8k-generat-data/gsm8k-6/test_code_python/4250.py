def solution():
    # Calculate the total number of chairs carried to the hall
    chairs_per_trip = 5  # each student carries 5 chairs per trip
    total_trips = 10  # they make a total of 10 trips
    total_students = 4 + 1  # Kingsley and her four friends
    total_chairs = chairs_per_trip * total_trips * total_students
    result = total_chairs
    return result

print(solution())