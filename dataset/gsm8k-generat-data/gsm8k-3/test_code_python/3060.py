def solution():
    """If it takes 10 people 10 days to shovel 10,000 pounds of coal, how many days will it take half of these ten people to shovel 40,000 pounds of coal?"""
    # Define initial variables
    people = 10
    days = 10
    coal = 10000

    # Calculate the amount of coal each person can shovel per day
    coal_per_person_per_day = coal / (people * days)

    # Calculate the number of people needed to shovel 40,000 pounds of coal
    half_people = people / 2

    # Calculate the number of days it will take half the people to shovel 40,000 pounds of coal
    half_coal = 40000
    half_days = half_coal / (half_people * coal_per_person_per_day)

    # Display the result
    result = half_days
    return result

print(solution())