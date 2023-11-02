def solution():
    num_flute_players = 5
    num_trumpet_players = num_flute_players * 3
    num_trombone_players = num_trumpet_players - 8
    num_drummers = num_trombone_players + 11
    num_clarinet_players = num_flute_players * 2
    num_french_horn_players = num_trombone_players + 3

    # Calculate the total number of band members
    total_members = num_flute_players + num_trumpet_players + num_trombone_players + num_drummers + num_clarinet_players + num_french_horn_players

    # Calculate the number of seats needed on the bus
    seats_needed = total_members
    result = seats_needed
    return result

print(solution())