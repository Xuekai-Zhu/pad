def solution():
    """Dan's skateboarding helmet has ten more craters than Daniel's ski helmet. Rin's snorkel helmet has 15 more craters than Dan's and Daniel's helmets combined. If Rin's helmet has 75 craters, how many craters are in Dan's helmet?"""
    # Let's represent the number of craters in Daniel's helmet as x
    x = 0
    # Dan's helmet has 10 more craters than Daniel's
    dan = x + 10
    # Rin's helmet has 15 more craters than Dan's and Daniel's helmets combined
    rin = dan + x + 15
    # Rin's helmet has 75 craters
    rin = 75
    # Find x (number of craters in Daniel's helmet)
    x = (rin - 10 - 15) / 2

    # Display the number of craters in Dan's helmet
    result = x
    return result

print(solution())