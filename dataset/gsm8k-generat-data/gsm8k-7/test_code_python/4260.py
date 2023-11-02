def solution():
    num_bridgette_guests = 84

    # Calculate the number of guests Alex is inviting
    num_alex_guests = num_bridgette_guests * (2/3)

    # Calculate the total number of guests at the wedding
    total_guests = num_bridgette_guests + num_alex_guests

    # Calculate the total number of plates needed (with extra plates)
    total_plates = total_guests + 10

    # Calculate the total number of asparagus spears needed for all the plates
    num_asparagus_spears = total_plates * 8

    result = num_asparagus_spears
    return result

print(solution())