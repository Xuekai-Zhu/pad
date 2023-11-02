def solution():
    # Define the ratio of the poodle's barks to the terrier's barks
    poodle_to_terrier_ratio = 2/1

    # Calculate the total number of barks before the terrier is hushed six times
    terrier_barks_before_hush = 2 * 6

    # Calculate the total number of barks the poodle makes before the dogs stop barking
    total_poodle_barks = poodle_to_terrier_ratio * terrier_barks_before_hush

    # Calculate the number of times the poodle barks
    poodle_barks = total_poodle_barks / 3
    result = poodle_barks
    return result

print(solution())