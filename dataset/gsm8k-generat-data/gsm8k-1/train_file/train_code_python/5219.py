def solution():
    """At the gym, every day, there are 300 towels laid out for guest use. Each guest is given 1 towel during their visit. The gym is open from 10:00 a.m. to 2:00 p.m. In the first hour, 50 guests enter the gym. In the second hour, 20% more guests enter than during the first hour. In the third hour, 25% more guests enter than in the second hour. In the fourth hour, one third more guests enter than in the third hour. In total, how many towels do they need to wash that evening?"""
    towels_per_guest = 1
    towels_laid_out = 300
    guests_hour_one = 50
    guests_hour_two = guests_hour_one * 1.2
    guests_hour_three = guests_hour_two * 1.25
    guests_hour_four = guests_hour_three * 1.3333333333333333
    total_guests = guests_hour_one + guests_hour_two + guests_hour_three + guests_hour_four
    total_towels_used = total_guests * towels_per_guest
    towels_to_wash = total_towels_used - towels_laid_out
    result = towels_to_wash
    return result

print(solution())