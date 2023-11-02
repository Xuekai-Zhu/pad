def solution():
    """A singer has 50 microphones that he wants to arrange in pairs on a stage. While making the arrangement, he realizes that 20% of the microphones won't find any space to fit in after arranging the rest in pairs. How many pairs of microphones was he able to arrange on the stage?"""
    total_microphones = 50
    arranged_microphones = total_microphones * 0.8
    pairs_of_microphones = arranged_microphones / 2
    result = pairs_of_microphones
    return result

print(solution())