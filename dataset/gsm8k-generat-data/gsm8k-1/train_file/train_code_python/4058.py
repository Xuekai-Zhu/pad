def solution():
    """Mike began to train to play basketball every day for a tournament. One day he plays a maximum of 2 hours. After a week of training, he increased the maximum time to 3 hours. How many hours did Mike train during the first two weeks?"""
    
    first_week_hours = 2 * 7 # He trained for 2 hours per day for 7 days in the first week
    second_week_hours = 3 * 7 # He trained for 3 hours per day for 7 days in the second week
    total_training_hours = first_week_hours + second_week_hours
    result = total_training_hours
    return result

print(solution())