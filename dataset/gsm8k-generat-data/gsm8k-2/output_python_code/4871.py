def solution():
    """Jill is the hairdresser for the school's dance team and has to braid 8 dancers' hair. If each dancer has five braids and each braid takes 30 seconds, how many minutes will it take to braid all the dancers' hair?"""
    dancers = 8
    braids_per_dancer = 5
    braid_time = 30 # seconds
    total_braids = dancers * braids_per_dancer
    total_time = (total_braids * braid_time) / 60 # convert to minutes
    result = total_time
    return result

print(solution())