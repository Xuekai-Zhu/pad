def solution():
    """Dan's skateboarding helmet has ten more craters than Daniel's ski helmet. Rin's snorkel helmet has 15 more craters than Dan's and Daniel's helmets combined. If Rin's helmet has 75 craters, how many craters are in Dan's helmet?"""
    rin_helmet = 75
    dan_and_daniel = (rin_helmet - 15) / 2
    dan_helmet = dan_and_daniel - 10
    result = dan_helmet
    return result

print(solution())