def solution():
    brother_height = 180
    mary_height = (2/3) * brother_height
    minimum_height = 140

    # Calculate the number of centimeters Mary needs to grow
    more_cm_needed = minimum_height - mary_height
    result = more_cm_needed
    return result

print(solution())