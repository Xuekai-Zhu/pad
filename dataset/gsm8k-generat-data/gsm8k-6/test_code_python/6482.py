def solution():
    # Calculate the number of turtles in the lake
    male_turtles = 40/100  # 60% turtles are female, hence only 40% turtles are male
    striped_turtles = male_turtles * (1/4)  # 1 in 4 male turtles have stripes
    baby_striped_turtles = striped_turtles * (4/100)  # 4 out of 100 striped turtles are babies
    adult_striped_turtles = striped_turtles * (60/100)  # 60% of striped turtles are adults
    total_turtles = 1/(baby_striped_turtles + adult_striped_turtles)  # Total number of turtles in the lake
    result = total_turtles
    return result

print(solution())