def solution():
    """Troy had 300 straws. He fed 3/5 of the straws to the adult pigs and an equal number of straws to the piglets. If there were 20 piglets, how many straws did each piglet eat?"""
    # Define the number of straws fed to the adult pigs
    adult_pig_straws = 300 * (3/5)

    # Define the total number of piglets
    piglet_count = 20

    # Define the total number of straws fed to the piglets
    piglet_straws = adult_pig_straws / piglet_count

    # Display the number of straws each piglet ate
    result = piglet_straws
    return result

print(solution())