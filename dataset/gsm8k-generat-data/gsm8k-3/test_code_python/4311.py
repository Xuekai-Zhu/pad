def solution():
    """There is a fruit display that has apples, oranges, and bananas.  There are twice as many apples as oranges, and there are twice as many oranges as bananas.  How many fruits are on the display in total if there are 5 bananas on the display?"""
    # Define the number of bananas on the display
    bananas = 5

    # Calculate the number of oranges on the display
    oranges = bananas * 2

    # Calculate the number of apples on the display
    apples = oranges * 2

    # Calculate the total number of fruits on the display
    total_fruits = bananas + oranges + apples

    # Display the total number of fruits
    result = total_fruits
    return result

print(solution())