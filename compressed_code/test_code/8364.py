def solution():
    
    total_sausages = 600
    monday_sausages = (2/5) * total_sausages
    remaining_sausages = total_sausages - monday_sausages
    tuesday_sausages = (1/2) * remaining_sausages
    remaining_sausages = remaining_sausages - tuesday_sausages
    friday_sausages = (3/4) * remaining_sausages
    remaining_sausages = remaining_sausages - friday_sausages
    result = remaining_sausages
    return result

print(solution())