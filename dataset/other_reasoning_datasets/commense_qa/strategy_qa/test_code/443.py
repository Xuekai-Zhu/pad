def solution():
    tandem_bike_seats = 2
    triples_tandem_bike_seats = 3
    apollo_15_crew_members = 3
    if triples_tandem_bike_seats >= apollo_15_crew_members:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())