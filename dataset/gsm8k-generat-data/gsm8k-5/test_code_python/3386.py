def solution():
    poodle_barks = 0
    terrier_barks = 0
    hush_count = 0

    while hush_count < 6:
        poodle_barks += 2
        terrier_barks += 1

        if terrier_barks % 2 == 0:  # Terrier barks are hushed every second time
            hush_count += 1

    result = poodle_barks
    return result

print(solution())