def solution():
    num_rounds = 30
    
    # Calculate the total possible points scored in all rounds
    total_possible_points = num_rounds * 5
    
    # Calculate Taro's score
    taro_score = (3/5) * total_possible_points - 4
    
    # Calculate Vlad's score by subtracting Taro's score from the total possible points
    vlad_score = total_possible_points - taro_score
    result = vlad_score
    return result

print(solution())