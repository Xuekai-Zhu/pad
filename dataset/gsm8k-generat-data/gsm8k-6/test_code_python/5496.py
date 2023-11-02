def solution():
    # Calculate the number of people on the trolley after each stop
    num_people = 10  # initial number of people
    num_people -= 3  # 3 people got off at the second stop
    num_people += 2*10  # twice as many people from the first stop got on at the second stop
    num_people -= 18  # 18 people got off at the third stop
    num_people += 2  # 2 people got on at the third stop
    result = num_people
    return result

print(solution())