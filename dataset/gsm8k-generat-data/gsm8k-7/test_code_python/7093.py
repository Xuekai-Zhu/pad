def solution():
    num_guests = 15
    num_glasses_per_person = 2
    ounces_per_glass = 12

    # Calculate the total number of glasses needed
    total_glasses = num_guests * num_glasses_per_person

    # Calculate the total number of ounces needed
    total_ounces = total_glasses * ounces_per_glass
    result = total_ounces
    return result

print(solution())