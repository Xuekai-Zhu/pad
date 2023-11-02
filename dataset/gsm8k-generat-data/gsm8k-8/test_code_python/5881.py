def solution():
    # Calculate the total miles driven in one week
    miles_to_work = 20 * 2 * 5  # 20 miles each way, 5 days a week
    miles_for_leisure = 40
    total_miles = miles_to_work + miles_for_leisure

    # Calculate the total gallons of gas used in one week
    mpg = 30
    gallons_per_mile = 1 / mpg
    total_gallons = total_miles * gallons_per_mile
    result = total_gallons
    return result

print(solution())