def solution():
    """In April, Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt. However, Emma gathered twice as many eggs as Tank in their second round of egg hunt, while Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round. If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs, and Emma gathered 60 eggs in the second egg hunt round, find the number of eggs that the 6 other egg hunters collected?"""
    
    # Emma's total from the first round
    Emma_first_round = 400 - (20 + 60 + 10)
    
    # Tank's total from the first round
    Tank_first_round = Emma_first_round + 10
    
    # Emma's total from the second round
    Emma_second_round = 60
    
    # Tank's total from the second round
    Tank_second_round = Emma_second_round / 2 - 20
    
    # 6 other people's total
    other_people = 400 - (Emma_second_round + Tank_second_round)

print(solution())