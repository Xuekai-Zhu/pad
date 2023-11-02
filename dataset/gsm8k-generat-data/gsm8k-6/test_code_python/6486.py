def solution():
    # Calculate the total distance Janet drives
    total_distance = 30 + 50 + 30 + 50  # 30 miles east to dermatologist, 50 miles west to gynecologist, and then back home again
    gallons_of_gas = total_distance / 20  # total distance divided by the car's gas mileage
    result = gallons_of_gas
    return result

print(solution())