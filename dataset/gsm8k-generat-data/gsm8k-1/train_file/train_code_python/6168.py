def solution():
    """Tomas is hoping to run a marathon next year, which is 26.3 miles. He knows that each month he trains, he can run twice as far as the month before. If he can run 3 miles during the first month of training, how many total months before the marathon should he start training to ensure he can run far enough?"""
    marathon_distance = 26.3
    current_distance = 3
    months = 1
    
    while current_distance < marathon_distance:
        current_distance *= 2
        months += 1
    
    result = months
    return result

print(solution())