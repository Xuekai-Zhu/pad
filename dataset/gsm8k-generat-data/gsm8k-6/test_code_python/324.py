def solution():
    # Calculate the number of rooms in the building
    total_rooms = 4 * 10  # 4 floors with 10 rooms each

    # Calculate the total number of hours Legacy will work
    total_hours = total_rooms * 6  # it takes 6 hours to clean one room, so total_hours = total_rooms * 6

    # Calculate the total amount of money Legacy will make
    total_pay = total_hours * 15  # Legacy earns $15 per hour of work

    result = total_pay
    return result

print(solution())