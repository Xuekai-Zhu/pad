def solution():
    """Brianna started out with a bag of 24 marbles. She lost four marbles through a hole in the bag. Then, she gave away twice as many marbles as she had lost through the hole in the bag. Finally, her dog ate half as many marbles as Brianna had lost through the hole in the bag. How many marbles did Brianna have remaining?"""
    
    initial_marbles = 24
    marbles_lost = 4
    marbles_given_away = 2 * marbles_lost
    marbles_eaten_by_dog = marbles_lost / 2
    
    remaining_marbles = initial_marbles - marbles_lost - marbles_given_away - marbles_eaten_by_dog
    
    result = remaining_marbles
    return result

print(solution())