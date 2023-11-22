def solution():
    
    # Define the number of hours Hallie had dance practice for each day
    tuesday_hours = 1
    thursday_hours = 2
    saturday_hours = tuesday_hours * 2

    # Calculate the total number of hours Hallie had dance practice for a week
    total_hours = (tuesday_hours + thursday_hours + saturday_hours) * 7

    # Display the total number of hours Hallie had dance practice for a week
    result = total_hours
    return result

print(solution())