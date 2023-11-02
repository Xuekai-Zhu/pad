def solution():
    poodle_barks = 0
    terrier_barks = 0
    hush_count = 0

    # Loop until the dogs stop barking
    while hush_count < 6:
        # Poodle barks twice for every one time the terrier barks
        poodle_barks += 2
        terrier_barks += 1

        # Terrier's owner hushes it every second time it barks
        if terrier_barks % 2 == 0:
            hush_count += 1

    # The last bark was by the poodle
    num_poodle_barks = hush_count + 1
    result = num_poodle_barks
    return result

print(solution())