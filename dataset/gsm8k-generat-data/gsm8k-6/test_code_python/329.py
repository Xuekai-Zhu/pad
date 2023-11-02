def solution():
    # Calculate the total number of doughnuts
    total_doughnuts = (2*12) + (3*12)  # Samuel bought 2 dozen and Cathy bought 3 dozen

    # Calculate the total number of people to share the doughnuts with
    total_people = 8 + 2  # Samuel and Cathy

    # Calculate the number of doughnuts each person receives
    doughnuts_per_person = total_doughnuts / total_people
    result = doughnuts_per_person
    return result

print(solution())