def solution():
    total_eggs = 3 * 12  # The family prepared 3 dozen boiled eggs

    num_adults = 3  # There are 3 adults in the family
    adult_eggs = 3 * num_adults  # Each adult gets 3 eggs

    num_girls = 7  # There are 7 girls in the family, and each gets 1 egg
    girl_eggs = num_girls

    # Calculate the total number of eggs given to the boys
    boy_eggs = total_eggs - adult_eggs - girl_eggs

    # Calculate the number of boys on the trip
    num_boys = boy_eggs / (num_girls + 1)

    result = num_boys
    return result

print(solution())