def solution():
    """If it takes 10 people 10 days to shovel 10,000 pounds of coal, how many days will it take half of these ten people to shovel 40,000 pounds of coal?"""
    total_people = 10
    total_days = 10
    total_coal = 10000
    half_people = total_people / 2
    target_coal = 40000
    shovel_rate = total_coal / (total_people * total_days)
    target_days = target_coal / (half_people * shovel_rate)
    result = target_days
    return result

print(solution())