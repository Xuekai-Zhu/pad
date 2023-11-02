def solution():
    starting_money = 9
    saved_money = 5
    frisbee_cost = 4
    puzzle_cost = 3
    friend_gift = 8
    
    # Calculate Oliver's total money after saving
    total_money = starting_money + saved_money
    
    # Subtract the costs of the frisbee and puzzle
    total_money -= frisbee_cost + puzzle_cost
    
    # Add the friend's gift
    total_money += friend_gift
    
    result = total_money
    return result

print(solution())