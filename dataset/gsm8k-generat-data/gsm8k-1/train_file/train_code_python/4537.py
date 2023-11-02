def solution():
    """At the end of a circus act, there are 12 dogs on stage. Half of the dogs are standing on their back legs and the other half are standing on all 4 legs. How many dog paws are on the ground?"""
    total_dogs = 12
    back_legs_per_dog = 2
    all_legs_per_dog = 4
    total_back_legs = (total_dogs / 2) * back_legs_per_dog
    total_paws_on_ground = total_back_legs + ((total_dogs / 2) * all_legs_per_dog)
    result = total_paws_on_ground
    return result

print(solution())