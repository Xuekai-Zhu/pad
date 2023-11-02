def solution():
    num_chocolate_bars = 20
    num_people = 6 # Matilda, her 4 sisters, and her father
    father_share = num_chocolate_bars / num_people
    num_chocolate_bars -= father_share * 5
    num_chocolate_bars -= 3 # mother's share
    num_chocolate_bars -= 2 # father ate 2
    result = num_chocolate_bars
    return result

print(solution())