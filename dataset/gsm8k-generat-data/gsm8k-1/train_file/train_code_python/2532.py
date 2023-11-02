def solution():
    """Matt's entire family was going to spend the week at the lake house for vacation. Matt's family included his mom, dad, his older brother and his wife and their 4 kids. His Uncle Joe and his wife were also coming and would bring their 3 kids. The house only sleeps 4 people. Everyone else would sleep 2 to a tent outside. How many tents would they need?"""
    num_people = 1 + 1 + 1 + 2 + 4 + 2 + 3
    num_beds = 4
    num_tents = (num_people - num_beds) / 2
    result = num_tents
    return result

print(solution())