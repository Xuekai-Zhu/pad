def solution():
    
    total_sausages = 600
    monday_eaten = 2/5 * total_sausages
    remaining_sausages = total_sausages - monday_eaten
    tuesday_eaten = 1/2 * remaining_sausages
    remaining_sausages = remaining_sausages - tuesday_eaten
    friday_saved = remaining_sausages
    friday_eaten = 3/4 * friday_saved
    remaining_sausages = friday_saved - friday_eaten
    result = remaining_sausages
    return result

print(solution())