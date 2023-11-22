def solution():
    
    # Define the number of boxes and marbles per box
    boxes = 5
    marbles_per_box = 50

    # Calculate the total number of marbles
    total_marbles = boxes * marbles_per_box

    # Subtract the marbles received from the friend
    remaining_marbles = total_marbles - 20

    # Display the remaining number of marbles
    result = remaining_marbles
    return result

print(solution())