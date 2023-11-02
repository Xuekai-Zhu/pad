def solution():
    # Given information
    juniper_whiskers = 12
    puffy_whiskers = 3 * juniper_whiskers
    scruffy_whiskers = 2 * puffy_whiskers
    total_whiskers = puffy_whiskers + scruffy_whiskers + juniper_whiskers

    # Calculate Buffy's whiskers
    buffy_whiskers = (total_whiskers - juniper_whiskers) / 3

    result = buffy_whiskers
    return result

print(solution())