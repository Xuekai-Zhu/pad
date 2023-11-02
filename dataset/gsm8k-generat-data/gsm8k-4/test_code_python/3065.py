def solution():
    """Tom originally was only able to lift 80  kg farmer handles per hand.  After some training, he was able to double this number.  He then decided to specialize and was able to get an extra 10%.  How much weight can he hold in total?"""
    # Define the original weight Tom can lift per hand
    original_weight = 80

    # Double the original weight after training
    doubled_weight = original_weight * 2

    # Add an extra 10% after specializing
    specialized_weight = doubled_weight * 1.1

    # Calculate the total weight Tom can hold
    total_weight = specialized_weight * 2

    result = total_weight
    return result

print(solution())