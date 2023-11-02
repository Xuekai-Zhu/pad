def solution():
    """The local aquarium has 4 dolphins that each require 3 hours of training daily. The aquarium has 2 trainers and they want to split the hours they spend training the dolphins equally. How many hours will each trainer spend training the dolphins?"""
    # Define the number of dolphins and hours of training per dolphin
    num_dolphins = 4
    hours_per_dolphin = 3

    # Define the number of trainers
    num_trainers = 2

    # Calculate the total hours of training needed per day
    total_hours = num_dolphins * hours_per_dolphin

    # Divide the total hours equally between the trainers
    hours_per_trainer = total_hours / num_trainers

    # Display the hours of training per trainer
    result = hours_per_trainer
    return result

print(solution())