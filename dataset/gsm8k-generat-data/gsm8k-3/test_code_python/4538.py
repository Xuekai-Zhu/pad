def solution():
    """At the end of a circus act, there are 12 dogs on stage.  Half of the dogs are standing on their back legs and the other half are standing on all 4 legs.  How many dog paws are on the ground?"""
    # Calculate the number of dogs standing on their back legs
    back_legs_dogs = 12 / 2

    # Calculate the number of dog paws on the ground
    paws_on_ground = (back_legs_dogs * 2) + ((12 - back_legs_dogs) * 4)

    # Display the number of dog paws on the ground
    result = paws_on_ground
    return result

print(solution())