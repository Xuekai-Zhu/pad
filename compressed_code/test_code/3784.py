def solution():
    
    starting_mileage = 1728
    gallons_per_fill = 20
    mpg = 30
    total_miles_driven = 0
    for i in range(2):
        total_miles_driven += gallons_per_fill * mpg

    final_mileage = starting_mileage + total_miles_driven
    result = final_mileage
    return result

print(solution())