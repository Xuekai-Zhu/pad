def solution():
    # Calculate the total distance Laura drives per week
    distance_to_house = 20  # 20-mile round trip from her school to her house
    distance_to_supermarket = distance_to_house + 10  # 10 miles farther away from the school
    total_distance = distance_to_house*5 + distance_to_supermarket*2  # drives to school every morning and two afternoons a week drives to the supermarket
    result = total_distance
    return result

print(solution())