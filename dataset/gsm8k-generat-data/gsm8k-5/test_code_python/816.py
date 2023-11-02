def solution():
    days_with_two_plates = 4  # Matt and his son use one plate each on three days, so the remaining four days require two plates each
    plates_per_day = 2*days_with_two_plates + 2*3  # Matt and his son each use one plate on three days, and everyone uses two plates on the remaining days
    plates_per_week = 7*plates_per_day  # Matt only wants to do dishes once a week, so he needs enough plates for the entire week

    result = plates_per_week
    return result

print(solution())