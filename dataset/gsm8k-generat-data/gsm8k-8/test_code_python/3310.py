def solution():
    # Calculate the total time in seconds
    total_time = 6 * 60

    # Calculate the gallons poured in during that time
    gallons_poured = (total_time / 20)

    # Calculate how many more gallons are needed to fill the tank
    remaining_gallons = 50 - gallons_poured

    result = remaining_gallons
    return result

print(solution())