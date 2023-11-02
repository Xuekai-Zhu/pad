def solution():
    veteran_park_cans = 24
    central_park_cans = (2 * veteran_park_cans - 8)  # 8 more than half of Veteran's Park cans
    central_park_cans = central_park_cans / 2  # half of Central Park cans moved to Veteran's Park
    veteran_park_cans += central_park_cans  # add moved Central Park cans to Veteran's Park
    result = veteran_park_cans
    return result

print(solution())