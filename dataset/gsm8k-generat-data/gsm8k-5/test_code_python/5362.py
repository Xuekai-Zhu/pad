def solution():
    norwich_carriages = 100  # Norwich has 100 carriages
    flying_scotsman_carriages = norwich_carriages + 20  # Flying Scotsman has 20 more carriages than Norwich
    euston_carriages = 130  # Euston has 130 carriages
    euston_carriages_difference = euston_carriages - 20  # Euston has 20 more carriages than Norfolk
    norfolk_carriages = euston_carriages_difference - norwich_carriages  # Calculate the number of carriages in Norfolk

    # Calculate the total number of carriages
    total_carriages = norwich_carriages + flying_scotsman_carriages + euston_carriages + norfolk_carriages
    result = total_carriages
    return result

print(solution())