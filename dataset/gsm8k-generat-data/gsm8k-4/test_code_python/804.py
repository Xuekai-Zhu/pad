def solution():
    """A zoo has 16 pandas, paired into mates (in the same zoo). Only 25% of the panda couples get pregnant after mating. If they each have one baby, how many panda babies are born?"""
    # Define the initial number of panda couples
    panda_couples = 16 // 2

    # Calculate the number of panda couples that get pregnant
    pregnant_couples = panda_couples * 0.25

    # Calculate the total number of panda babies born
    panda_babies = pregnant_couples * 1

    # Return the result
    result = panda_babies
    return result

print(solution())