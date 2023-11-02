def solution():
    total_homes = 200  # Kiaan has to deliver newspapers to 200 homes
    homes_delivered_first_hour = 2/5 * total_homes  # Kiaan delivered newspapers to 2/5 of the homes in first hour
    homes_remaining_first_hour = total_homes - homes_delivered_first_hour  # Kiaan has this many homes left to deliver

    # In the second hour, Kiaan delivers newspapers to 60% of remaining homes
    homes_delivered_second_hour = 0.60 * homes_remaining_first_hour  
    homes_remaining_second_hour = homes_remaining_first_hour - homes_delivered_second_hour  # Kiaan has this many homes left to deliver

    total_homes_delivered = homes_delivered_first_hour + homes_delivered_second_hour  # Kiaan delivered newspapers to this many homes
    homes_remaining = total_homes - total_homes_delivered  # Kiaan has to deliver newspapers to this many homes
    result = homes_remaining
    return result

print(solution())