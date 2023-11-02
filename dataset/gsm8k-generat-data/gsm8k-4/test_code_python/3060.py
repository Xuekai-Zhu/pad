def solution():
    """If it takes 10 people 10 days to shovel 10,000 pounds of coal, how many days will it take half of these ten people to shovel 40,000 pounds of coal?"""
    # Define the initial amount of coal and the number of people
    initial_coal = 10000
    initial_people = 10

    # Calculate the amount of coal each person can shovel per day
    rate_per_person = initial_coal / (initial_people * 10)

    # Calculate the number of days it would take half the people to shovel 40000 pounds of coal
    new_people = initial_people / 2
    new_coal = 40000
    days = new_coal / (new_people * rate_per_person)

    result = days
    return result

print(solution())