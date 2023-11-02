def solution():
    total_meat = 20  # Jackson had 20 kilograms of meat
    meatballs = total_meat * (1/4)  # Jackson used 1/4 of the meat to make meatballs
    spring_rolls = 3  # Jackson used 3 kilograms of meat to make spring rolls

    # Calculate the remaining meat
    remaining_meat = total_meat - meatballs - spring_rolls
    result = remaining_meat
    return result

print(solution())