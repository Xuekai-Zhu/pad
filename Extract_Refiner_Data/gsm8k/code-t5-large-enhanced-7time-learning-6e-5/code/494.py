def solution():
    
    # Define the number of oranges each box has
    ASHNES_ORANGES = 10
    BRIANNE_ORANGES = ASHNES_ORANGES + 20

    # Calculate the total number of oranges brought by Ashley and Brianne
    total_oranges = (ASHNES_ORANGES + BRIANNE_ORANGES) * 5

    # Calculate the number of greek orange pies that can be made
    pies = total_oranges // 3

    # Display the number of greek orange pies they can make
    result = pies
    return result

print(solution())