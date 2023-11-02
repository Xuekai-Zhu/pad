def solution():
    """Andy started out the year weighing 156 pounds. He then grew 3 inches and gained 36 pounds. Andy wasn't happy with his weight and decided to exercise. Over the next 3 months, he lost an eighth of his weight every month. How much less does Andy weigh now than at the beginning of the year?"""
    # Define Andy's starting weight and weight loss per month
    starting_weight = 156
    weight_loss = starting_weight / 8

    # Calculate Andy's weight after gaining 36 pounds
    new_weight = starting_weight + 36

    # Calculate Andy's weight after losing one-eighth of his weight for 3 months
    for i in range(3):
        new_weight -= weight_loss

    # Calculate the difference between Andy's current weight and his starting weight
    weight_difference = starting_weight - new_weight

    # Display the weight difference
    result = weight_difference
    return result

print(solution())