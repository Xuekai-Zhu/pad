def solution():
    # Define the number of towels available and the number of guests in each hour
    towels_available = 300
    guests_hour1 = 50
    guests_hour2 = 1.2 * guests_hour1
    guests_hour3 = 1.25 * guests_hour2
    guests_hour4 = 1.33 * guests_hour3

    # Calculate the total number of guests for the day
    total_guests = guests_hour1 + guests_hour2 + guests_hour3 + guests_hour4

    # Calculate the total number of towels used
    total_towels_used = total_guests

    # Calculate the number of towels that need to be washed
    towels_to_wash = total_towels_used - towels_available

    result = towels_to_wash
    return result

print(solution())