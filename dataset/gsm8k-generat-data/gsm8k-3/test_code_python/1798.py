def solution():
    """John injures his shoulder while lifting weights.  After the injury, his bench press goes down 80%.  After a bit of training, he manages to triple the weight he can bench.  If he started with a 500-pound bench press, what is it now?"""
    # Define John's starting bench press weight
    starting_weight = 500

    # Calculate John's bench press weight after the injury
    injured_weight = starting_weight * 0.2

    # Calculate John's bench press weight after training
    final_weight = injured_weight * 3

    # Display John's final bench press weight
    result = final_weight
    return result

print(solution())