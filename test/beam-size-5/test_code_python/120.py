def solution():
    
    # Define the total number of letters in the pile
    total_letters = 60

    # Define the number of already-stamped letters
    already_stamped_letters = 30

    # Calculate the number of stamps on one-third of the letters needing stamps
    stamps_on_third = already_stamped_letters / 3

    # Calculate the number of stamps in the pile
    stamps_in_pile = total_letters - already_stamped_letters - stamps_on_third

    # Display the number of stamps in the pile
    result = stamps_in_pile
    return result

print(solution())