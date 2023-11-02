def solution():
    """If it takes 10 people 10 days to shovel 10,000 pounds of coal, how many days will it take half of these ten people to shovel 40,000 pounds of coal?"""
    people = 10
    days = 10
    coal = 10000
    half_people = people / 2
    required_coal = 40000
    # Calculate the amount of coal that one person can shovel in one day
    coal_per_person_per_day = coal / (people * days)
    # Calculate the number of days needed for half the people to shovel the required amount of coal
    days_needed = required_coal / (half_people * coal_per_person_per_day)
    result = days_needed
    return result

print(solution())