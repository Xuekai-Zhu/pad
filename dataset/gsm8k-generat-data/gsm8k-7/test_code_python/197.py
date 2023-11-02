def solution():
    num_people = 16
    num_rolls = 40

    #Calculate the number of people eating 1 1/2 rolls each
    half_people = num_people // 2
    num_half_people_roll = half_people * (3/2)

    #Calculate the number of people eating 1/2 a roll each
    num_other_people_roll = (num_people - half_people) * (1/2)

    #Calculate the total number of rolls eaten
    total_rolls_eaten = num_half_people_roll + num_other_people_roll

    #Calculate the number of rolls leftover
    num_rolls_leftover = num_rolls - total_rolls_eaten
    result = num_rolls_leftover
    return result

print(solution())