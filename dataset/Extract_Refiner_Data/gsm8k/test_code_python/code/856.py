def solution():
    
    # Define the initial number of oranges
    oranges = 12

    # Subtract the oranges given to the daughters
    oranges -= 3 * 2

    # Subtract the oranges given to the boy
    oranges -= 3

    # return the result
    result = oranges
    return result

print(solution())