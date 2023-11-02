def solution():
    # Define the number of guests and glasses per guest
    num_guests = 120
    num_glasses_per_guest = 2
    
    # Calculate the total number of glasses needed
    total_glasses = num_guests * num_glasses_per_guest
    
    # Calculate the number of bottles needed, rounding up to the nearest whole number
    bottles_needed = math.ceil(total_glasses / 6)
    
    result = bottles_needed
    return result

print(solution())