def solution():
    towels_per_guest = 1  # Each guest is given 1 towel
    total_towels = 300  # There are 300 towels laid out for guest use every day
    guests_hour_1 = 50  # 50 guests enter the gym in the first hour
    guests_hour_2 = round(guests_hour_1 * 1.2)  # 20% more guests enter the gym in the second hour
    guests_hour_3 = round(guests_hour_2 * 1.25)  # 25% more guests enter the gym in the third hour
    guests_hour_4 = round(guests_hour_3 * 1.33)  # one third more guests enter the gym in the fourth hour

    # Calculate the total number of towels needed
    total_guests = guests_hour_1 + guests_hour_2 + guests_hour_3 + guests_hour_4
    total_towels_needed = total_guests * towels_per_guest

    # Calculate the number of towels that need to be washed
    towels_to_wash = total_towels_needed - total_towels
    result = towels_to_wash
    return result

print(solution())