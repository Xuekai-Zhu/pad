def solution():
    """A pair of dogs are barking back and forth at each other from across the street. The poodle barks twice for every one time the terrier barks. The terrier’s owner hushes it every second time it barks. She has to say “hush” six times before the dogs stopped barking. How many times did the poodle bark?"""
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