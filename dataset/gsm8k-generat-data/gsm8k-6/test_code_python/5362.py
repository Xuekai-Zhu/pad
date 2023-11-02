def solution():
    norfolk_carriages = 130 - 20  # Euston has 20 more carriages than Norfolk, so we subtract 20 from Euston's carriages to get Norfolk's carriages
    flying_scotsman_carriages = 100 + 20  # Flying Scotsman has 20 more carriages than Norwich
    total_carriages = norfolk_carriages + flying_scotsman_carriages + 130  # add up the carriages from all three towns
    result = total_carriages
    return result

print(solution())