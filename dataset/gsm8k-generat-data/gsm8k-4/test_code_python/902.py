def solution():
    """Troy had 300 straws. He fed 3/5 of the straws to the adult pigs and an equal number of straws to the piglets. If there were 20 piglets, how many straws did each piglet eat?"""
    # Define the total number of straws
    total_straws = 300

    # Calculate the number of straws fed to adult pigs
    adult_pig_straws = total_straws * 0.6

    # Calculate the number of straws fed to each piglet
    piglet_straws = adult_pig_straws / 20

    # Return the result
    result = piglet_straws
    return result

print(solution())