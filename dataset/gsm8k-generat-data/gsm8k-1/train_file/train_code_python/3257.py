def solution():
    """Mr Castiel prepared 600 boar sausages on the weekend. He ate 2/5 of them on Monday, half of the remaining on Tuesday and saved the rest for Friday. If he ate 3/4 of the remaining boar sausages on Friday, how many sausages are left?"""
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