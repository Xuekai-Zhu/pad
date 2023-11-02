def solution():
    # Calculate the number of people on the bus after the third stop
    total_people = 50 - 15 - 8 + 2 - 4 + 3  # 15 people got off at the first stop, 8 got off and 2 got on at the second stop, 4 got off and 3 got on at the third stop
    result = total_people
    return result

print(solution())