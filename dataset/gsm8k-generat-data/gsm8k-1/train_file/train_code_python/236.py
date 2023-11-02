def solution():
    """In April, Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt. However, Emma gathered twice as many eggs as Tank in their second round of egg hunt, while Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round. If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs, and Emma gathered 60 eggs in the second egg hunt round, find the number of eggs that the 6 other egg hunters collected?"""
    # First round number of eggs
    tank_1st_round = emma_1st_round + 10
    
    # Total number of eggs gathered in the second round
    total_2nd_round = 2*tank_2nd_round + emma_2nd_round - 20
    
    # Total number of eggs gathered by Tank and Emma
    tank_and_emma = tank_1st_round + tank_2nd_round + emma_1st_round + emma_2nd_round
    
    # Total number of eggs gathered by the 8 people
    total_eggs = tank_and_emma + 60 + 6*x
    
    # Equation to solve for x
    8*x = 400 - total_eggs
    
    # Solution for x
    x = (400 - total_eggs) / 8
    
    result = x
    return result

print(solution())