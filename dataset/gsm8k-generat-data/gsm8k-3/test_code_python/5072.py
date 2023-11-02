def solution():
    """Erica sees 9 butterflies in the garden.  She sees one-third of them fly away.  How many butterflies are left in the garden?"""
    # Define the initial number of butterflies
    initial_butterflies = 9

    # Calculate the number of butterflies that flew away
    butterflies_flew_away = initial_butterflies // 3

    # Calculate the number of butterflies remaining
    butterflies_remaining = initial_butterflies - butterflies_flew_away

    # Display the number of butterflies remaining
    result = butterflies_remaining
    return result

print(solution())