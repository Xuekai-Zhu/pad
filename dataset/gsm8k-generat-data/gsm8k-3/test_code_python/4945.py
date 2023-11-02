def solution():
    """300 cows in a field are made up of male and female cows. There are twice as many females as males. Half the females are spotted, and half the males have horns. How many more females with spots are there than males with horns?"""
    # Calculate the number of males and females
    males = 300 / 3
    females = males * 2

    # Calculate the number of females with spots
    females_spotted = females / 2

    # Calculate the number of males with horns
    males_horned = males / 2

    # Calculate the difference between the number of females with spots and males with horns
    difference = females_spotted - males_horned

    # Display the difference
    result = difference
    return result

print(solution())