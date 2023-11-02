def solution():
    # Calculate Mike's total pamphlets before break
    mikes_first_shift = 600 * 9
    # Calculate Mike's total pamphlets after break
    mikes_second_shift = 600 * 2 * 1/3
    # Calculate Leo's total pamphlets
    leos_shift = (600 * 9) / 3 * 2

    # Calculate the total pamphlets both printed
    total_pamphlets = mikes_first_shift + mikes_second_shift + leos_shift

    result = total_pamphlets
    return result

print(solution())