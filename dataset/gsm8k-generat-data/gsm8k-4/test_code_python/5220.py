def solution():
    """At the gym, every day, there are 300 towels laid out for guest use. Each guest is given 1 towel during their visit. The gym is open from 10:00 a.m. to 2:00 p.m. In the first hour, 50 guests enter the gym. In the second hour, 20% more guests enter than during the first hour. In the third hour, 25% more guests enter than in the second hour. In the fourth hour, one third more guests enter than in the third hour. In total, how many towels do they need to wash that evening?"""
    # Define the number of towels available for guest use
    towels_available = 300

    # Calculate the number of guests in the first hour
    guests_hour_1 = 50

    # Calculate the number of guests in the second hour
    guests_hour_2 = guests_hour_1 * 1.2

    # Calculate the number of guests in the third hour
    guests_hour_3 = guests_hour_2 * 1.25

    # Calculate the number of guests in the fourth hour
    guests_hour_4 = guests_hour_3 * 4/3

    # Calculate the total number of guests
    total_guests = guests_hour_1 + guests_hour_2 + guests_hour_3 + guests_hour_4

    # Calculate the total number of towels needed
    towels_needed = total_guests

    # Calculate the number of towels that need to be washed
    towels_to_wash = towels_needed - towels_available

    # return the result
    result = towels_to_wash
    return result

print(solution())