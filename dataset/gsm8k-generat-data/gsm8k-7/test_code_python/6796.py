def solution():
    total_bottles = 35
    jason_bought = 5
    harry_bought = 6

    # Calculate the total number of bottles bought by Jason and Harry
    total_bought = jason_bought + harry_bought

    # Calculate the number of bottles left on the store shelf
    bottles_left = total_bottles - total_bought
    result = bottles_left
    return result

print(solution())