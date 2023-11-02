def solution():
    # Calculate the total number of beds in the hotel
    beds_in_two_bedrooms = 8 * 2
    beds_in_three_bedrooms = (13 - 8) * 3
    total_beds = beds_in_two_bedrooms + beds_in_three_bedrooms
    result = total_beds
    return result

print(solution())