def solution():
    """Farmer Brown raises emus, large birds. His flock has a total of 60 heads and legs. How many emus are in his flock?"""
    # Let e be the number of emus in the flock
    # Each emu has 2 legs and 1 head
    # Each non-emu bird (such as a chicken) has 2 legs and 1 head
    # Therefore, the total number of heads in the flock is e, and the total number of legs is 2e

    # We can write the equation: 2e = 60 + 2*(total non-emu birds)

    # Since we don't know how many non-emu birds there are, we can't solve for e exactly.
    # However, we can use some trial and error to find a value of e that makes sense.

    # If there were no non-emu birds, then e = 30 (since there are 60 legs total). However, this is unlikely.
    # If there were 1 non-emu bird, then e = 29 (since there would be 58 legs from the emus and 2 from the non-emu bird).
    # This seems unlikely as well, since it's hard to have a flock with only one non-emu bird.
    # If there were 2 non-emu birds, then e = 28 (since there would be 56 legs from the emus and 4 from the non-emu birds).
    # This is a possibility, but we should keep going to check.
    # If there were 3 non-emu birds, then e = 27 (since there would be 54 legs from the emus and 6 from the non-emu birds).
    # This is also a possibility, but we should keep going to check.
    # If there were 4 non-emu birds, then e = 26 (since there would be 52 legs from the emus and 8 from the non-emu birds).
    # This seems unlikely, since we're getting further away from the starting value of 30.

    # So, the most likely values of e are 28 or 27. We can't determine the exact value without more information.
    # We'll return both possibilities as a tuple.
    result = (28, 27)
    return result

print(solution())