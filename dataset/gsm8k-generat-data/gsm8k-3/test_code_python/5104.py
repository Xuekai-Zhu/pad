def solution():
    """The school band is going to a competition. Five members play the flute. There are three times as many members who play the trumpet. There are eight fewer trombone players than trumpeters, and eleven more drummers than trombone players. There are twice as many members that play the clarinet as members that play the flute. Three more members play the French horn than play the trombone. How many seats are needed on the bus?"""
    # Define the number of members for each instrument
    FLUTE_MEMBERS = 5
    TRUMPET_MEMBERS = 3 * FLUTE_MEMBERS
    TROMBONE_MEMBERS = TRUMPET_MEMBERS - 8
    DRUM_MEMBERS = TROMBONE_MEMBERS + 11
    CLARINET_MEMBERS = 2 * FLUTE_MEMBERS
    HORN_MEMBERS = TROMBONE_MEMBERS + 3

    # Calculate the total number of members in the band
    total_members = FLUTE_MEMBERS + TRUMPET_MEMBERS + TROMBONE_MEMBERS + DRUM_MEMBERS + CLARINET_MEMBERS + HORN_MEMBERS

    # Calculate the number of seats needed on the bus
    seats_needed = total_members

    # Display the number of seats needed
    result = seats_needed
    return result

print(solution())