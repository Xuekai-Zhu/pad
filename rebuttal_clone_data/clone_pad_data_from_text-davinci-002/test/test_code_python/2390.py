def solution():
    tourists = 30
    anaconda_victims = 2
    non_poisoned_tourists = tourists - anaconda_victims
    poisoned_tourists = non_poisoned_tourists / 2
    recovered_tourists = poisoned_tourists / 7
    tour_end_tourists = non_poisoned_tourists - poisoned_tourists + recovered_tourists
    result = tour_end_tourists
    
    return result

print(solution())