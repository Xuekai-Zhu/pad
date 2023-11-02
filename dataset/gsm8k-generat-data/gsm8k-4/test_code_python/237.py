def solution():
    """In April, Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt. However, Emma gathered twice as many eggs as Tank in their second round of egg hunt, while Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round. If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs, and Emma gathered 60 eggs in the second egg hunt round, find the number of eggs that the 6 other egg hunters collected?"""
    
    # Calculate the total number of eggs Tank and Emma gathered together
    # Let x be the number of eggs Tank gathered in the first round
    # Then, Emma gathered x-10 eggs in the first round and 2(x-20) eggs in the second round
    # The total number of eggs Tank and Emma gathered together is x + (x-10) + 2(x-20) = 4x - 50
    # If the total number of eggs in the pile was 400 and Emma gathered 60 in the second round, then Tank and Emma gathered 400 - 60 = 340 eggs together in the first round and Tank gathered (340 - 60)/3 = 93.33 eggs in the first round
    # We can assume that Tank gathered 93 eggs in the first round and Emma gathered 80 eggs in the first round and 40 eggs in the second round
    
    # Calculate the total number of eggs gathered by the 6 other egg hunters
    total_eggs = 400
    tank_first_round = 93
    emma_first_round = 80
    emma_second_round = 40
    tank_second_round = tank_first_round - 20
    
    total_tank = tank_first_round + tank_second_round
    total_emma = emma_first_round + emma_second_round
    total_tank_emma = total_tank + total_emma
    total_other_hunters = total_eggs - total_tank_emma
    result = total_other_hunters
    return result

print(solution())