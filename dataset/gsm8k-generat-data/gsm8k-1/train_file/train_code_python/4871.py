def solution():
    """Jill is the hairdresser for the school's dance team and has to braid 8 dancers' hair. If each dancer has five braids and each braid takes 30 seconds, how many minutes will it take to braid all the dancers' hair?"""
    dancers = 8
    braids_per_dancer = 5
    time_per_braid = 30 # in seconds
    total_time = dancers * braids_per_dancer * time_per_braid / 60 # convert to minutes
    result = total_time
    return result

print(solution())