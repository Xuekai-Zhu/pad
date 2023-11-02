def solution():
    """Barbie enjoys buying jewelry. One day, she bought 12 pairs of earrings, and gave half of them to Alissa, making Alissa's total number of collections to be triple the number of earrings she was given. How many earrings does Alissa have now?"""
    barbie_earrings = 12 * 2  # since one pair has 2 earrings
    alissa_earrings = barbie_earrings / 2
    alissa_collections = alissa_earrings * 3
    result = alissa_collections
    return result

print(solution())