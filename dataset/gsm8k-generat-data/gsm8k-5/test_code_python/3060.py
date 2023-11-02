def solution():
    # Calculate the rate at which the 10 people shovel coal
    rate = 10000/10/10  # 10000 pounds of coal, 10 people, 10 days

    # Calculate the number of days it will take half the people to shovel 40000 pounds of coal
    days = 40000/(rate*(10/2))

    result = days
    return result

print(solution())