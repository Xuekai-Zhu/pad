def solution():
    # Each person has 2 roller skates, which means 4 wheels per person
    wheels_per_person = 4
    # Total number of people skating is 40
    total_people = 40
    # Total number of wheels on the floor is the product of the two variables above
    total_wheels = wheels_per_person * total_people
    result = total_wheels
    return result

print(solution())