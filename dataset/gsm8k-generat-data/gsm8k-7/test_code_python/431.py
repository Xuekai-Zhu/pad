def solution():
    num_people = 5  # Javier, wife, and 3 children
    num_dogs = 2
    num_cats = 1
    num_legs_per_person = 2  # Assuming all humans have 2 legs
    num_legs_per_dog = 4
    num_legs_per_cat = 4

    # Calculate the total number of legs from all humans
    total_human_legs = num_people * num_legs_per_person

    # Calculate the total number of legs from all dogs
    total_dog_legs = num_dogs * num_legs_per_dog

    # Calculate the total number of legs from the cat
    total_cat_legs = num_cats * num_legs_per_cat

    # Calculate the total number of legs in the household
    total_legs = total_human_legs + total_dog_legs + total_cat_legs
    result = total_legs
    return result

print(solution())