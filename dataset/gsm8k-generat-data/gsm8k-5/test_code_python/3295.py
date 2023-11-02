def solution():
    # Each person has 2 legs, so 16 legs in the pool belong to 8 people
    # 8 people in the pool means that there are 10 people in the house in total
    total_people = 10

    # Karen, Donald, Tom, and Eva are adults, so there are 4 adults in the house
    adults = 4

    # The 4 adults have a total of 10 children between them
    children = 10

    # The total number of people in the house is the sum of adults and children
    total_in_house = adults + children

    # The number of people not in the pool is the total number of people in the house minus the 8 people in the pool
    not_in_pool = total_in_house - 8
    result = not_in_pool
    return result

print(solution())