def solution():
    # Calculate the number of craters in Dan's helmet
    total_craters = 75  # given Rin's helmet has 75 craters
    dan_rin_craters = total_craters - 15  # given Rin's helmet has 15 more craters than Dan's and Daniel's combined
    dan_craters = (dan_rin_craters - 10) / 2  # given Dan's helmet has 10 more craters than Daniel's
    result = dan_craters
    return result

print(solution())