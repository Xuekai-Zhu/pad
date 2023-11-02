def solution():
    
    initial_tourists = 30
    anaconda_victims = 2
    remaining_tourists = initial_tourists - anaconda_victims
    poisoned_tourists = remaining_tourists / 2
    recovered_tourists = poisoned_tourists / 7
    remaining_tourists -= poisoned_tourists - recovered_tourists
    result = remaining_tourists
    return result

print(solution())