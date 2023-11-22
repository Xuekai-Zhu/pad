def solution():
    
    # Define the capacity of the hospital and the number of occupied beds
    capacity = 1000
    occupied_beds = capacity * (1/5)

    # Calculate the total number of beds occupied after 2 weeks
    total_occupied_beds = occupied_beds * 50 * 7 * 2

    # Calculate the total number of unoccupied beds
    total_unoccupied_beds = total_occupied_beds - capacity

    # return the result
    result = total_unoccupied_beds
    return result

print(solution())