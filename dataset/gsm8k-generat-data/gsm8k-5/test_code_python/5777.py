def solution():
    bone_in_chicken = 16  # Peter is buying 16 pounds of bone-in chicken
    hamburgers = bone_in_chicken / 2  # Peter is buying half the amount of hamburgers as bone-in chicken
    hot_dogs = hamburgers + 2  # Peter is buying 2 more pounds of hot dogs than hamburgers
    sides = hot_dogs / 2  # Peter is buying sides that weigh half the amount of hot dogs

    # Calculate the total amount of food Peter will buy
    total_food = bone_in_chicken + hamburgers + hot_dogs + sides
    result = total_food
    return result

print(solution())