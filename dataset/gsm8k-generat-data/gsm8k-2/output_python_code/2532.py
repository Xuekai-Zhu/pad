def solution():
    """Matt's entire family was going to spend the week at the lake house for vacation. Matt's family included his mom, dad, his older brother and his wife and their 4 kids. His Uncle Joe and his wife were also coming and would bring their 3 kids. The house only sleeps 4 people. Everyone else would sleep 2 to a tent outside. How many tents would they need?"""
    family_size = 1 + 1 + 1 + 2 + 4 + 2 + 2 + 3 + 2
    house_capacity = 4
    tent_capacity = 2
    remaining_people = family_size - house_capacity
    number_of_tents = remaining_people // tent_capacity + 1
    result = number_of_tents
    return result

print(solution())