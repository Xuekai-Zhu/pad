def solution():
    original_typing_speed = 212
    carpal_tunnel_decrease = 40
    new_typing_speed = original_typing_speed - carpal_tunnel_decrease
    num_words = 3440

    # Calculate the time it would take to type all the words at the original typing speed
    time_original = num_words / original_typing_speed

    # Calculate the time it would take to type all the words at the decreased typing speed
    time_decreased = num_words / new_typing_speed

    # Return the maximum of the two times as the final answer
    result = max(time_original, time_decreased)
    return result

print(solution())