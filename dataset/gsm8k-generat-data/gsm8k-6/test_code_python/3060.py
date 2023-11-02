def solution():
    # Calculate the coal shoveling rate of each person in pounds per day
    coal_rate = 1000 / 10 / 10  # 10 people shoveling 10,000 pounds of coal in 10 days

    # Calculate the number of days it would take half of the ten people to shovel 40,000 pounds of coal
    half_people_days = 40000 / (coal_rate * 5)  # half of 10 people shoveling 40,000 pounds of coal
    result = half_people_days
    return result

print(solution())