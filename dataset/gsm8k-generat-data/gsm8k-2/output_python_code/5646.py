def solution():
    """Carol fills up her gas tank as she is driving home for college, which is 220 miles away. She can get 20 miles to the gallon in her car, which has a 16-gallon gas tank. How many more miles will she be able to drive after she gets home and without filling her tank again?"""
    total_gas = 16
    gas_per_mile = 1/20
    distance_to_college = 220
    gas_used_to_college = distance_to_college * gas_per_mile
    gas_left = total_gas - gas_used_to_college
    remaining_distance = gas_left * 20
    result = remaining_distance
    return result

print(solution())