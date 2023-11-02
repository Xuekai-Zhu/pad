def solution():
    # Define the variables
    total_people = 7
    total_chalk = 3 * total_people
    extra_chalk = 12
    lost_chalk = 2
    
    # Calculate the original amount of chalk Erika and her siblings had
    original_chalk = (total_chalk - extra_chalk + lost_chalk) / 4
    
    result = original_chalk
    return result

print(solution())