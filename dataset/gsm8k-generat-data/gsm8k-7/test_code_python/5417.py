def solution():
    start_weight = 99
    initial_loss = 12
    gain_after_loss = 2 * initial_loss
    second_loss = 3 * initial_loss
    final_gain = initial_loss / 2

    # Calculate Mary's weight after initial loss
    current_weight = start_weight - initial_loss

    # Calculate Mary's weight after adding back initial loss and twice the gain
    current_weight += initial_loss + gain_after_loss

    # Calculate Mary's weight after dropping three times initial loss
    current_weight -= second_loss

    # Calculate Mary's weight after gaining back half a dozen pounds
    current_weight += final_gain

    result = current_weight
    return result

print(solution())