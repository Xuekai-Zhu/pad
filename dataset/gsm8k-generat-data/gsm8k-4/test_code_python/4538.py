def solution():
    """At the end of a circus act, there are 12 dogs on stage. Half of the dogs are standing on their back legs and the other half are standing on all 4 legs. How many dog paws are on the ground?"""
    # Define the number of dogs standing on their back legs and on all 4 legs
    back_legs_dogs = 6
    four_legs_dogs = 6

    # Calculate the total number of dog paws on the ground
    paws_on_ground = back_legs_dogs * 2 + four_legs_dogs * 4

    # Display the result
    result = paws_on_ground
    return result

print(solution())