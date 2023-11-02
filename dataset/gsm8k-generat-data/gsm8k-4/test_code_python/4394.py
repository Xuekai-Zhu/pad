def solution():
    """Dan's skateboarding helmet has ten more craters than Daniel's ski helmet. Rin's snorkel helmet has 15 more craters than Dan's and Daniel's helmets combined. If Rin's helmet has 75 craters, how many craters are in Dan's helmet?"""
    # Define the number of craters in Rin's helmet
    rin_craters = 75

    # Calculate the total number of craters in Dan and Daniel's helmets combined
    dan_daniel_craters = (rin_craters - 15) / 2

    # Calculate the number of craters in Dan's helmet
    dan_craters = dan_daniel_craters - 10

    # Return the result
    result = dan_craters
    return result

print(solution())