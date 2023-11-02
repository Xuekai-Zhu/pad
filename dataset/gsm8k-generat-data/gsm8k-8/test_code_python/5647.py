def solution():
    # Calculate how many miles Carol can travel on a full tank of gas
    miles_per_tank = 20 * 16

    # Calculate how many miles Carol used to drive home
    miles_to_college = 220

    # Calculate how many miles Carol will have left in her tank after driving home
    miles_left = miles_per_tank - miles_to_college

    result = miles_left
    return result

print(solution())