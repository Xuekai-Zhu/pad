def solution():
    
    # Define the amount lost on the first race
    race1_loss = 5

    # Define the amount won on the second race
    race2_loss = 2 * race1_loss + 1

    # Define the amount lost on the third race
    race3_loss = 1.5 * race2_loss

    # Calculate the total loss
    total_loss = race1_loss + race2_loss + race3_loss

    # Calculate the average loss per day
    average_loss = total_loss / 3

    # Display the average loss
    result = average_loss
    return result

print(solution())