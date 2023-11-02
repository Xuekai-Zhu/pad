def solution():
    capacity = 1000  # The hospital has a capacity of 1000 beds
    occupied_beds = capacity / 5  # The hospital has 1/5 occupied beds
    patients_admitted = 50  # 50 patients are admitted into the hospital each day
    days = 14  # There are 14 days in a week

    # Calculate the total number of occupied beds after 2 weeks
    total_occupied_beds = occupied_beds * days

    # Calculate the total number of unoccupied beds after 2 weeks
    total_unoccupied_beds = capacity - total_occupied_beds
    result = total_unoccupied_beds
    return result

print(solution())