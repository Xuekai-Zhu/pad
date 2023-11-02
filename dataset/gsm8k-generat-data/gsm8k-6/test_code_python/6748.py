def solution():
    juniper_whiskers = 12
    puffy_whiskers = 3 * juniper_whiskers
    scruffy_whiskers = 2 * puffy_whiskers
    total_whiskers = puffy_whiskers + scruffy_whiskers + juniper_whiskers
    buffy_whiskers = total_whiskers / 4
    result = buffy_whiskers
    return result

print(solution())