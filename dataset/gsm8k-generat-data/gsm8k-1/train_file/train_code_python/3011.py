def solution():
    """Amber is baking cakes for her party. She has invited 8 friends and each one will want two slices of cake. Each cake makes 6 slices. If she bakes 4 cakes, how many slices will be left over at the end if she eats three herself?"""
    guests = 8
    slices_per_guest = 2
    total_slices_needed = guests * slices_per_guest
    slices_per_cake = 6
    cakes_baked = 4
    total_slices = slices_per_cake * cakes_baked
    slices_left = total_slices - (total_slices_needed + 3)
    result = slices_left
    return result

print(solution())