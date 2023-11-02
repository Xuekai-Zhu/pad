def solution():
    billy_spit_distance = 30
    madison_spit_distance = billy_spit_distance * 1.2  # Madison can spit 20% farther than Billy
    ryan_spit_distance = madison_spit_distance * 0.5   # Ryan can spit 50% shorter than Madison
    result = ryan_spit_distance
    return result

print(solution())