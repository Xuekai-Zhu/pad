def solution():
    bottles_in_fridge = 4
    bottles_in_pantry = 4
    bottles_bought = 5
    bottles_consumed = 3

    # Calculate the total number of bottles Martha has
    total_bottles = bottles_in_fridge + bottles_in_pantry + bottles_bought

    # Calculate the total number of bottles left after consumption
    bottles_left = total_bottles - bottles_consumed
    result = bottles_left
    return result

print(solution())