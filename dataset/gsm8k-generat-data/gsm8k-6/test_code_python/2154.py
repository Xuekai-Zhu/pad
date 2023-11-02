def solution():
    # Calculate the total number of family units the spacecraft can carry
    full_capacity = 300

    # Calculate the number of family units the spacecraft will carry when it leaves the earth
    carrying_capacity = (1/3) * full_capacity - 100

    # Calculate the number of people on the ship when it leaves the earth
    starting_people = carrying_capacity * 4
    result = starting_people
    return result

print(solution())