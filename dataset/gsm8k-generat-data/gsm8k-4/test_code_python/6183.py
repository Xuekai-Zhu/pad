def solution():
    """The local aquarium has 4 dolphins that each require 3 hours of training daily. The aquarium has 2 trainers and they want to split the hours they spend training the dolphins equally. How many hours will each trainer spend training the dolphins?"""
    # Define the number of dolphins and the hours of training required per dolphin
    dolphins = 4
    hours_per_dolphin = 3

    # Define the number of trainers
    trainers = 2

    # Calculate the total hours of training required
    total_hours = dolphins * hours_per_dolphin

    # Divide the total hours of training equally between the trainers
    hours_per_trainer = total_hours / trainers

    # return the result
    result = hours_per_trainer
    return result

print(solution())