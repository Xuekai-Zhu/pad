def solution():
    num_children = 45  # given there were 45 children
    num_adults = num_children * 3  # given adults were one third as many as children
    
    num_blue = num_adults // 3  # given one third of adults wore blue
    num_not_blue = num_adults - num_blue  # calculate the number of adults who did not wear blue
    
    result = num_not_blue
    return result

print(solution())