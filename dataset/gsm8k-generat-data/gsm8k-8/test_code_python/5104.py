def solution():
    # Define the number of members playing each instrument
    flute = 5
    trumpet = 3 * flute
    trombone = trumpet - 8
    drum = trombone + 11
    clarinet = 2 * flute
    french_horn = trombone + 3

    # Calculate the total number of members
    total_members = flute + trumpet + trombone + drum + clarinet + french_horn

    # Calculate the number of seats needed on the bus
    seats_needed = total_members + 10
    result = seats_needed
    return result

print(solution())