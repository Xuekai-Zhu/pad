def solution():
    # Define the number of craters in Daniel's helmet
    daniel_craters = x

    # Calculate the number of craters in Dan's helmet
    dan_craters = daniel_craters + 10

    # Calculate the combined number of craters in Dan's and Daniel's helmets
    combined_craters = dan_craters + daniel_craters

    # Calculate the number of craters in Rin's helmet
    rin_craters = combined_craters + 15

    # Solve for x using the given information that Rin's helmet has 75 craters
    x = (rin_craters - 15 - dan_craters) / 2

    result = dan_craters
    return result

print(solution())