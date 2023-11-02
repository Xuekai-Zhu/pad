def solution():
    
    poodle_barks = 0
    terrier_barks = 0
    terrier_hushes = 0
    hushes_needed = 6

    while terrier_hushes < hushes_needed:
        poodle_barks += 2
        terrier_barks += 1

        if terrier_barks % 2 == 0:
            terrier_hushes += 1

    result = poodle_barks
    return result

print(solution())