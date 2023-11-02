def solution():
    """Mr Castiel prepared 600 boar sausages on the weekend. He ate 2/5 of them on Monday, half of the remaining
    on Tuesday and saved the rest for Friday. If he ate 3/4 of the remaining boar sausages on Friday, how many sausages are left?"""
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