def solution():
    """In April, Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt. However, Emma gathered twice as many eggs as Tank in their second round of egg hunt, while Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round. If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs, and Emma gathered 60 eggs in the second egg hunt round, find the number of eggs that the 6 other egg hunters collected?"""
    
    # Define Emma's number of eggs in the second round
    emma_second_round = 60

    # Calculate Tank's number of eggs in the second round
    tank_second_round = emma_second_round / 2 - 20

    # Calculate Tank's number of eggs in the first round
    tank_first_round = tank_second_round - 10

    # Calculate Emma's number of eggs in the first round
    emma_first_round = tank_first_round + 10

    # Calculate the total number of eggs gathered by Tank and Emma
    tank_and_emma_total = tank_first_round + tank_second_round + emma_first_round + emma_second_round

    # Calculate the number of eggs gathered by the 6 other egg hunters
    other_hunters_total = 400 - tank_and_emma_total

    result = other_hunters_total
    return result

print(solution())