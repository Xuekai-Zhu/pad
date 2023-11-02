def solution():
    # Find the number of girls who joined the field trip
    girls_on_trip = 18 // 2 - 8  # half of the students are girls and 8 are boys

    # Find the number of girls who were not able to join the field trip
    girls_not_on_trip = 18 // 2 - girls_on_trip

    result = girls_not_on_trip
    return result

print(solution())