def solution():
    rin_helmet_craters = 75
    dan_ski_helmet_craters = None

    # Calculate the number of craters in Dan's skateboarding helmet
    dan_skate_helmet_craters = rin_helmet_craters - 15

    # Calculate the number of craters in Daniel's ski helmet
    daniel_ski_helmet_craters = dan_skate_helmet_craters - 10

    # Calculate the number of craters in Dan's helmet
    dan_ski_helmet_craters = daniel_ski_helmet_craters + 10

    result = dan_ski_helmet_craters
    return result

print(solution())