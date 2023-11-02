def solution():
    """A pair of dogs are barking back and forth at each other from across the street. The poodle barks twice for every one time the terrier barks. The terrier’s owner hushes it every second time it barks. She has to say “hush” six times before the dogs stopped barking. How many times did the poodle bark?"""
    # Define the ratio of barks between the poodle and terrier
    bark_ratio = 2

    # Initialize counters for the number of barks from each dog and the number of times the terrier was hushed
    poodle_barks = 0
    terrier_barks = 0
    terrier_hushes = 0

    # Loop until both dogs have barked a total of 6 times
    while poodle_barks + terrier_barks < 6:
        # The poodle barks twice for every one time the terrier barks, so add 2 to the poodle's barks
        poodle_barks += bark_ratio

        # Add 1 to the terrier's barks
        terrier_barks += 1

        # Hush the terrier every second time it barks
        if terrier_barks % 2 == 0:
            terrier_hushes += 1

    # The total number of terrier barks is the sum of the barks and hushes
    total_terrier_barks = terrier_barks + terrier_hushes

    # Subtract the terrier barks from the total to get the number of poodle barks
    poodle_barks = poodle_barks - total_terrier_barks

    result = poodle_barks
    return result

print(solution())