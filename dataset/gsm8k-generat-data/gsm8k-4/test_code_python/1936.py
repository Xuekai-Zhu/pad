def solution():
    """Josh gets together with 7 friends. Everyone including him puts 5 dollars into a pot.
    First place gets 80% of the money. Second and third place split the rest.
    How much money does third place get?"""
    
    # Define the number of participants and the amount of money each person puts into the pot
    num_participants = 8
    each_contribution = 5
    
    # Calculate the total amount of money in the pot
    total_pot = num_participants * each_contribution
    
    # Calculate the amount of money for first place
    first_place = 0.8 * total_pot
    
    # Calculate the remaining amount of money
    remaining_money = total_pot - first_place
    
    # Calculate the amount of money for second and third place (split evenly)
    second_third_place = remaining_money / 2
    
    # Calculate the amount of money for third place
    third_place = second_third_place
    
    result = third_place
    return result

print(solution())