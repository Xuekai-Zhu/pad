def solution():
    starting_dogs = 200
    incoming_dogs = 100
    adopted_weekly = 40
    adopted_monthly = 60
    
    # Calculate the total number of dogs after the incoming dogs arrive
    total_dogs = starting_dogs + incoming_dogs
    
    # Calculate the number of dogs left after a week of adoptions
    dogs_left_weekly = total_dogs - adopted_weekly
    
    # Calculate the number of dogs left after a month of adoptions
    dogs_left_monthly = dogs_left_weekly - adopted_monthly
    
    result = dogs_left_monthly
    return result

print(solution())