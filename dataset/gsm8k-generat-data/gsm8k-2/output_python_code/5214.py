def solution():
    """Anya washes 32 hairs down the drain when she washes her hair and brushes out half that amount when she brushes it.
    How many hairs does Anya have to grow back to always have one more hair than she started with after washing, brushing, and growing it?"""
    starting_hair = 100  # Assuming Anya starts with 100 hairs for simplicity
    hairs_washed = 32
    hairs_brushed = hairs_washed / 2
    hairs_remaining = starting_hair - hairs_washed + hairs_brushed
    hairs_needed_to_grow_back = starting_hair - hairs_remaining + 1
    result = hairs_needed_to_grow_back
    return result

print(solution())