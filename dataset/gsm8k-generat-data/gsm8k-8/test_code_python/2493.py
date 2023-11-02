def solution():
    # Calculate the amount of ingredients per person
    eggs_per_person = 2 / 4
    milk_per_person = 4 / 4

    # Calculate the total amount of ingredients for 8 people
    eggs_for_eight = eggs_per_person * 8
    milk_for_eight = milk_per_person * 8

    # Calculate the number of eggs Tyler needs to buy
    eggs_needed = eggs_for_eight - 3
    result = eggs_needed
    return result

print(solution())