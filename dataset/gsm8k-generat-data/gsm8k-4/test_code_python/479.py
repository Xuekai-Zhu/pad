def solution():
    """Kat decides she wants to start a boxing career. She gets a gym membership and spends 1 hour in the gym 3 times a week doing strength training. She also trained at the boxing gym 4 times a week for 1.5 hours. How many hours a week does she train?"""
    # Define the number of hours spent doing strength training
    strength_training_hours = 1 * 3

    # Define the number of hours spent training at the boxing gym
    boxing_hours = 1.5 * 4

    # Calculate the total number of hours spent training
    total_training_hours = strength_training_hours + boxing_hours

    # return the total number of hours spent training
    result = total_training_hours
    return result

print(solution())