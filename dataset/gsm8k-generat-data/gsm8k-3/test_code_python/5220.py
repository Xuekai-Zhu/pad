def solution():
    """At the gym, every day, there are 300 towels laid out for guest use.  Each guest is given 1 towel during their visit.  The gym is open from 10:00 a.m. to 2:00 p.m. In the first hour, 50 guests enter the gym.  In the second hour, 20% more guests enter than during the first hour.  In the third hour, 25% more guests enter than in the second hour.  In the fourth hour, one third more guests enter than in the third hour.  In total, how many towels do they need to wash that evening?"""
    # Define necessary variables
    towels_used = 0
    total_guests = 0

    # Calculate number of guests in each hour
    guests_1 = 50
    guests_2 = round(guests_1 * 1.2)
    guests_3 = round(guests_2 * 1.25)
    guests_4 = round(guests_3 * 1.33)

    # Calculate total number of guests
    total_guests = guests_1 + guests_2 + guests_3 + guests_4

    # Calculate number of towels used
    towels_used = total_guests

    # Calculate number of towels to wash
    towels_to_wash = towels_used - 300

    # Display number of towels to wash
    result = towels_to_wash
    return result

print(solution())