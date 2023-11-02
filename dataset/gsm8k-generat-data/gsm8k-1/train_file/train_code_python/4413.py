def solution():
    """John climbs up 3 flights of stairs. Each flight is 10 feet. He then climbs a rope that is half that height. Finally, he climbs a ladder that is 10 feet longer than the rope. How high up did he go?"""
    
    flights = 3
    flight_height = 10
    rope_height = flight_height / 2
    ladder_height = rope_height + 10
    total_height = (flights * flight_height) + rope_height + ladder_height
    
    result = total_height
    return result

print(solution())