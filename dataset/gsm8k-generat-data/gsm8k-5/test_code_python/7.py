def solution():
    weight_jelly_beans = 1/2  # Each pound of jelly beans weighs 0.5 pounds
    weight_brownies = 1  # Each pound of brownies weighs 1 pound
    weight_gummy_worms = 2  # Each pound of gummy worms weighs 2 pounds

    # Calculate the weight after adding the jelly beans
    weight = 2  # The box weighed 2 pounds initially
    weight += weight_jelly_beans * 2  # Ken added 2 pounds of jelly beans

    # Calculate the weight after adding the brownies
    weight *= 3  # Ken added brownies until the weight tripled

    # Calculate the weight after adding the gummy worms
    weight += weight_gummy_worms * weight

    result = weight
    return result

print(solution())