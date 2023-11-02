def solution():
    
    total_dolphins = 20
    fully_trained = total_dolphins // 4
    remaining_dolphins = total_dolphins - fully_trained
    training_now = (2/3) * remaining_dolphins
    training_next_month = remaining_dolphins - training_now
    result = training_next_month
    return result

print(solution())