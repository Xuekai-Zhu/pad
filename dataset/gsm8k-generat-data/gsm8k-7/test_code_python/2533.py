def solution():
    num_people = 12 # Matt's family + Uncle Joe's family
    num_bedrooms = 1 # The house only sleeps 4
    num_tents = (num_people - num_bedrooms*4) / 2 # Everyone else sleeps 2 to a tent
    result = num_tents
    return result

print(solution())