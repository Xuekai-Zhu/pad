def solution():
    eyes = 3
    wrinkles = eyes * 3
    spots = wrinkles * 7
    total = eyes + wrinkles + spots
    lizard_eyes = eyes
    lizard_spots = spots
    lizard_wrinkles = wrinkles
    difference = total - (lizard_eyes + lizard_spots + lizard_wrinkles)
    result = difference
    return result

print(solution())