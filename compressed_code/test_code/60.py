def solution():
    
    total_loss = 103
    first_loss = 27
    second_loss = first_loss - 7
    remaining_loss = total_loss - first_loss - second_loss
    each_remaining_loss = remaining_loss / 2
    result = each_remaining_loss
    return result

print(solution())