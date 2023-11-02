def solution():
    # Calculate the number of plates needed for three days a week
    plates_for_three_days = 2 * 3  # Matt and his son use 1 plate each, so 2 plates are needed for 3 days

    # Calculate the number of plates needed for the remainder of the days
    plates_for_remainder_days = 2 * 4  # Matt, his son, and his parents use 2 plates each on 4 days

    # Calculate the total number of plates needed
    total_plates = plates_for_three_days + plates_for_remainder_days
    result = total_plates
    return result

print(solution())