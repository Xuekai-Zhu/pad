def solution():
    # Calculate the number of legs for each member of the household
    javier_legs = 2
    wife_legs = 2
    child_legs = 2 * 3
    dog_legs = 4 * 2
    cat_legs = 4

    # Calculate the total number of legs
    total_legs = javier_legs + wife_legs + child_legs + dog_legs + cat_legs
    result = total_legs
    return result

print(solution())