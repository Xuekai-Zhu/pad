def solution():
    total_butterflies = 9  # Erica sees 9 butterflies in the garden
    flown_away = total_butterflies / 3  # Erica sees one-third of them fly away

    # Calculate the number of butterflies left in the garden
    butterflies_left = total_butterflies - flown_away
    result = butterflies_left
    return result

print(solution())