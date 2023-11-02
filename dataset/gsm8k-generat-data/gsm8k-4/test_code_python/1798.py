def solution():
    """John injures his shoulder while lifting weights. After the injury, his bench press goes down 80%. After a bit of training, he manages to triple the weight he can bench. If he started with a 500-pound bench press, what is it now?"""
    # Define the initial bench press weight
    initial_weight = 500

    # Calculate the weight after the injury
    injured_weight = initial_weight * 0.2

    # Calculate the weight after training
    trained_weight = injured_weight * 3

    # return the result
    result = trained_weight
    return result

print(solution())