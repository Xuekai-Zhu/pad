def solution():
    joey_weight_lost = 8  # Joey loses 8 pounds in 4 weeks
    sandy_weight_lost = joey_weight_lost / 4  # Sandy wants to lose the same amount of weight as Joey
    weeks_to_lose_same_weight = sandy_weight_lost / joey_weight_lost  # Calculate the number of weeks it will take Sandy to lose the same amount of weight
    result = weeks_to_lose_same_weight
    return result

print(solution())