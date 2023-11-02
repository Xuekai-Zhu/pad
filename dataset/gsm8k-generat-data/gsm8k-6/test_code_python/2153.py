def solution():
    # Calculate the number of times Felicia has to fill her 1/4 cup measuring scoop
    flour = 2  # cups of flour needed
    white_sugar = 1  # cup of white sugar needed
    brown_sugar = 0.25  # 1/4 cup of brown sugar needed
    oil = 0.5  # 1/2 cup of oil needed
    total_cups = flour + white_sugar + brown_sugar + oil
    times_to_fill = total_cups * 4  # 1 cup = 4 scoops of 1/4 cup
    result = times_to_fill
    return result

print(solution())