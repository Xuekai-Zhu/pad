def solution():
    # Calculate the number of floors in Building B
    floors_buildingB = 4 + 9  # Building B has 9 more floors than Building A

    # Calculate the number of floors in Building C
    floors_buildingC = 5*floors_buildingB - 6  # Building C has six less than five times as many floors as Building B

    result = floors_buildingC
    return result

print(solution())