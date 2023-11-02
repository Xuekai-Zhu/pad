def solution():
    # Define the total number of bottles on the shelf
    total_bottles = 35

    # Jason buys 5 bottles
    jason_buys = 5

    # Harry buys 6 more bottles
    harry_buys = 6

    # Calculate the number of bottles left on the shelf
    bottles_left = total_bottles - jason_buys - harry_buys
    result = bottles_left
    return result

print(solution())