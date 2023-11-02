def solution():
    # Calculate the net loss of hairs per hair wash and brush
    hairs_lost = 32 + (1/2 * 32)  # Anya washes 32 hairs down the drain and brushes out half that amount

    # Calculate the number of hairs Anya needs to grow back after each hair wash and brush
    hairs_to_grow_back = hairs_lost + 1  # Anya wants to always have one more hair than she started with

    result = hairs_to_grow_back
    return result

print(solution())