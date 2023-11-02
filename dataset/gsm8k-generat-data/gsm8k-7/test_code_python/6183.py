def solution():
    num_dolphins = 4
    hours_per_dolphin = 3
    num_trainers = 2

    # Calculate the total number of hours needed to train all dolphins in one day
    total_hours = num_dolphins * hours_per_dolphin

    # Divide the total hours equally between the two trainers
    hours_per_trainer = total_hours / num_trainers
    result = hours_per_trainer
    return result

print(solution())