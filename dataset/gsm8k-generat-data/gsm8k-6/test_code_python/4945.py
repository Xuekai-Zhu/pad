def solution():
    # Calculate the number of male cows in the field
    num_males = 300 / 3  # Since there are twice as many females as males, there are three parts (2 females and 1 male) in a group of 3 cows

    # Calculate the number of female cows in the field
    num_females = 2 * num_males

    # Calculate the number of female cows with spots
    num_spotted_females = num_females / 2

    # Calculate the number of male cows with horns
    num_horned_males = num_males / 2

    # Calculate the difference between the number of females with spots and males with horns
    difference = num_spotted_females - num_horned_males
    result = difference
    return result

print(solution())