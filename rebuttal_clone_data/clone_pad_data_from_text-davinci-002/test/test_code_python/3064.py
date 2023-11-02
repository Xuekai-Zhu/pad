def solution():
    starting_weight = 99
    first_loss = 12
    second_gain = first_loss * 2
    third_loss = first_loss * 3
    fourth_gain = first_loss / 2
    final_weight = starting_weight - first_loss + second_gain - third_loss + fourth_gain
    result = final_weight
    return result

print(solution())