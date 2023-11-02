def solution():
    # Calculate the number of students who wore colored lipstick
    colored_lipstick = 200 / 2  # half of the students wore colored lipstick

    # Calculate the number of students who wore red lipstick
    red_lipstick = colored_lipstick / 4   # one quarter of the colored lipstick wearers wore red lipstick

    # Calculate the number of students who wore blue lipstick
    blue_lipstick = red_lipstick / 5 # one-fifth as many students wearing blue lipstick as were wearing red lipstick

    result = blue_lipstick
    return result

print(solution())