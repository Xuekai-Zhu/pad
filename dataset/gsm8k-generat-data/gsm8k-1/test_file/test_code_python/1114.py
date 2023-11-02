def solution():
    """In Tate’s garden pond, there are 4 male guppies, 7 female guppies, 3 male goldfishes, and 5 female goldfishes. He buys 2 male guppies, 1 female guppy, 2 male goldfishes, and 3 female goldfishes. How many more female fishes than male fishes does Tate have?"""
    initial_male_guppies = 4
    initial_female_guppies = 7
    initial_male_goldfishes = 3
    initial_female_goldfishes = 5

    added_male_guppies = 2
    added_female_guppies = 1
    added_male_goldfishes = 2
    added_female_goldfishes = 3

    total_male_fish = initial_male_guppies + initial_male_goldfishes + added_male_guppies + added_male_goldfishes
    total_female_fish = initial_female_guppies + initial_female_goldfishes + added_female_guppies + added_female_goldfishes

    difference = total_female_fish - total_male_fish
    result = difference

    return result

print(solution())