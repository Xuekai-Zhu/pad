def solution():
    num_people = 10
    num_days = 10
    total_coal = 10000
    new_coal = 40000
    half_people = num_people / 2

    # Calculate the amount of coal each person can shovel in one day
    rate = total_coal / (num_people * num_days)

    # Calculate the number of days it will take half the people to shovel the new amount of coal
    new_num_days = (new_coal / (half_people * rate))

    result = new_num_days
    return result

print(solution())