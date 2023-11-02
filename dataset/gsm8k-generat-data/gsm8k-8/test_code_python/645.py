def solution():
    # Calculate the number of floors with 6 apartments
    floors_with_6_apartments = 12 // 2

    # Calculate the number of floors with 5 apartments
    floors_with_5_apartments = 12 - floors_with_6_apartments

    # Calculate the total number of apartments
    total_apartments = (floors_with_6_apartments * 6) + (floors_with_5_apartments * 5)

    # Calculate the maximum number of residents
    max_residents = total_apartments * 4
    result = max_residents
    return result

print(solution())