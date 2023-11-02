def solution():
    """Tom weighs 150 kg. He manages to hold 1.5 times his weight in each hand while wearing a weight vest weighing half his weight. How much total weight was he moving with?"""
    # Define Tom's weight
    weight_tom = 150

    # Calculate the weight Tom can hold in each hand
    weight_each_hand = weight_tom * 1.5

    # Calculate the weight of the weight vest
    weight_vest = weight_tom / 2

    # Calculate the total weight Tom was moving with
    total_weight = weight_each_hand * 2 + weight_vest

    result = total_weight
    return result

print(solution())