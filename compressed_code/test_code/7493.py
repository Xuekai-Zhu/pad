def solution():
    
    billy_distance = 30
    madison_percent_increase = 0.2
    madison_distance = billy_distance * (1 + madison_percent_increase)
    ryan_percent_decrease = 0.5
    ryan_distance = madison_distance * (1 - ryan_percent_decrease)
    result = ryan_distance
    return result

print(solution())