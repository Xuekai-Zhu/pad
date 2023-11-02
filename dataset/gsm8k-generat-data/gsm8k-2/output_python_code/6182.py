def solution():
    """The local aquarium has 4 dolphins that each require 3 hours of training daily. The aquarium has 2 trainers and they want to split the hours they spend training the dolphins equally. How many hours will each trainer spend training the dolphins?"""
    total_dolphin_hours = 4 * 3
    total_trainer_hours = total_dolphin_hours / 2
    hours_per_trainer = total_trainer_hours / 2
    result = hours_per_trainer
    return result

print(solution())