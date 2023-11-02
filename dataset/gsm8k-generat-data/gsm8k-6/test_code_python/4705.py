def solution():
    meat = 20  # kilograms of meat
    meatballs = (1/4) * meat  # kilograms of meat used for meatballs
    remaining_meat = meat - meatballs - 3  # kilograms of meat remaining after making meatballs and spring rolls
    result = remaining_meat
    return result

print(solution())