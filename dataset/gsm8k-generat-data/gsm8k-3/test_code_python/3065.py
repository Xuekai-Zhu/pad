def solution():
    """Tom originally was only able to lift 80  kg farmer handles per hand.  After some training, he was able to double this number.  He then decided to specialize and was able to get an extra 10%.  How much weight can he hold in total?"""
    # Define Tom's original weight and the percentage increase after training
    ORIGINAL_WEIGHT = 80
    TRAINING_INCREASE = 2
    SPECIALIZATION_INCREASE = 0.1

    # Calculate Tom's weight after training
    training_weight = ORIGINAL_WEIGHT * TRAINING_INCREASE

    # Calculate Tom's weight after specialization
    specialization_weight = training_weight * (1 + SPECIALIZATION_INCREASE)

    # Calculate Tom's total weight
    total_weight = specialization_weight * 2 # since he lifts with each hand

    # Display Tom's total weight
    result = total_weight
    return result

print(solution())