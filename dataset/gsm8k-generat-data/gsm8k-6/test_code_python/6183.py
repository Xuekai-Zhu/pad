def solution():
    # Calculate the total number of training hours required daily
    total_hours = 4 * 3  # 4 dolphins each require 3 hours of training daily
    
    # Divide the total training hours equally between 2 trainers
    hours_per_trainer = total_hours / 2

    result = hours_per_trainer
    return result

print(solution())