def solution():
    # Calculate the number of guests in each hour
    guests_hour_1 = 50
    guests_hour_2 = int(guests_hour_1 * 1.2)  # 20% more guests enter than during the first hour
    guests_hour_3 = int(guests_hour_2 * 1.25)  # 25% more guests enter than in the second hour
    guests_hour_4 = int(guests_hour_3 * 1.33)  # one third more guests enter than in the third hour

    # Calculate the total number of guests in 4 hours
    total_guests = guests_hour_1 + guests_hour_2 + guests_hour_3 + guests_hour_4

    # Calculate the number of towels used and therefore needing to be washed
    towels_used = min(total_guests, 300)  # only 300 towels are provided, so the number of towels used cannot exceed 300

    result = towels_used
    return result

print(solution())