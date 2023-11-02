def solution():
    # Calculate the rate at which one person can shovel coal per day
    total_people = 10
    total_days = 10
    total_coal = 10000
    one_person_rate = total_coal / (total_people * total_days)

    # Calculate how long half of these people will take to shovel 40,000 pounds of coal
    half_people = total_people / 2
    new_total_coal = 40000
    new_total_days = new_total_coal / (half_people * one_person_rate)
    result = new_total_days
    return result

print(solution())