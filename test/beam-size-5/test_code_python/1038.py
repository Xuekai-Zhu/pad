def solution():
    
    first_race_loss = 5
    second_race_loss = 2 * first_race_loss + 1
    third_race_loss = 1.5 * second_race_loss
    total_loss = first_race_loss + second_race_loss + third_race_loss
    average_loss = total_loss / 3
    result = average_loss
    return result

print(solution())