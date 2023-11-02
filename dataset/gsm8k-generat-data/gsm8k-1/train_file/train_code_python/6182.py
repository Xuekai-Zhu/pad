def solution():
    """The local aquarium has 4 dolphins that each require 3 hours of training daily. The aquarium has 2 trainers and they want to split the hours they spend training the dolphins equally. How many hours will each trainer spend training the dolphins?"""
    dolphins = 4
    daily_hours_per_dolphin = 3
    total_daily_hours = dolphins * daily_hours_per_dolphin
    trainers = 2
    hours_per_trainer = total_daily_hours / trainers
    result = hours_per_trainer
    return result

print(solution())