def solution():
    
    # Define the number of letters in the pile of stamps
    pile_stamps = 60

    # Define the number of letters in the pile of already stamped letters
    already_stamped_letters = 30

    # Calculate the number of letters that need stamps
    stamps_needed = pile_stamps / 3

    # Calculate the total number of letters in the pile when Jennie began
    total_letters = pile_stamps + already_stamped_letters

    # Display the total number of letters in the pile when Jennie began
    result = total_letters
    return result

print(solution())