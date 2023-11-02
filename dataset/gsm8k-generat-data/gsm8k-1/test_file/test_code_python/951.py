def solution():
    """A hospital has a capacity of 1000 beds with 1/5 occupied. Due to the coronavirus outbreak, 50 patients are admitted into the hospital each day. Calculate the total number of unoccupied beds in the hospital after 2 weeks."""
    total_beds = 1000
    occupied_beds = total_beds / 5
    unoccupied_beds = total_beds - occupied_beds
    patients_per_day = 50
    days_in_2_weeks = 14
    total_patients = patients_per_day * days_in_2_weeks
    remaining_unoccupied_beds = unoccupied_beds - total_patients
    result = remaining_unoccupied_beds
    return result

print(solution())