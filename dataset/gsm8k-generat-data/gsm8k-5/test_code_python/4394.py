def solution():
    rin_craters = 75  # Rin's helmet has 75 craters
    dan_and_daniel_craters = rin_craters - 15  # Dan and Daniel's helmets combined have 15 less craters than Rin's
    dan_craters = (dan_and_daniel_craters - 10) / 2  # Dan's helmet has 10 less craters than Daniel's, and they have an equal number of craters

    result = dan_craters
    return result

print(solution())