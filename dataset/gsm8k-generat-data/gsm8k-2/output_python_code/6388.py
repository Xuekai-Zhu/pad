def solution():
    """Central Park had 8 more than half of the number of trash cans as in Veteran's Park. Then one night, someone took half of the trash cans from Central Park and put them in Veteran's Park. If originally there were 24 trash cans in Veteran's Park, how many trash cans are now in Veteran's Park?"""
    vet_park_cans = 24
    cp_cans = 2 * (vet_park_cans - 8)
    cp_cans_remaining = cp_cans / 2
    vet_park_cans += cp_cans_remaining
    result = vet_park_cans
    return result

print(solution())