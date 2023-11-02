def solution():
    """At the gym, every day, there are 300 towels laid out for guest use. Each guest is given 1 towel during their visit. The gym is open from 10:00 a.m. to 2:00 p.m. In the first hour, 50 guests enter the gym. In the second hour, 20% more guests enter than during the first hour. In the third hour, 25% more guests enter than in the second hour. In the fourth hour, one third more guests enter than in the third hour. In total, how many towels do they need to wash that evening?"""
    towels_per_guest = 1
    total_towels = 300
    guests_in_hour1 = 50
    guests_in_hour2 = guests_in_hour1 * 1.2
    guests_in_hour3 = guests_in_hour2 * 1.25
    guests_in_hour4 = guests_in_hour3 * 1.33
    total_guests = guests_in_hour1 + guests_in_hour2 + guests_in_hour3 + guests_in_hour4
    towels_needed = total_guests * towels_per_guest - total_towels
    result = towels_needed
    return result

print(solution())