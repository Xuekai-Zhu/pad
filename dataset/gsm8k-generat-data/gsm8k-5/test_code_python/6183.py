def solution():
    dolphins_per_trainer = 2  # Each trainer will train 2 dolphins
    daily_training_hours_per_dolphin = 3  # Each dolphin requires 3 hours of training daily

    # Calculate the total daily training hours for all dolphins
    total_training_hours = 4 * dolphins_per_trainer * daily_training_hours_per_dolphin

    # Divide the total training hours equally between the two trainers
    training_hours_per_trainer = total_training_hours / 2
    result = training_hours_per_trainer
    return result

print(solution())