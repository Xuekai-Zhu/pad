def solution():
    # Calculate the number of onions Brittney can chop in 30 minutes 
    onions_chopped_by_Brittney_in_30_min = (15/5) * 30 

    # Calculate the number of onions Carl can chop in 30 minutes 
    onions_chopped_by_Carl_in_30_min = (20/5) * 30 

    # Calculate the difference between the onions chopped by Carl and Brittney in 30 minutes 
    difference_in_onions_chopped = onions_chopped_by_Carl_in_30_min - onions_chopped_by_Brittney_in_30_min 

    result = difference_in_onions_chopped
    return result

print(solution())