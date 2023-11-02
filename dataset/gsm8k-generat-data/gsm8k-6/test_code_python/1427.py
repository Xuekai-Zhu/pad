def solution():
    # Calculate the remaining number of dogs after the last adoptions
    total_dogs = 200  # total number of dogs at the rescue center
    new_dogs = 100  # number of dogs brought in from another rescue center
    adopted_weekly = 40  # number of dogs adopted after one week
    adopted_monthly = 60  # number of dogs adopted after a month
    remaining_dogs = total_dogs + new_dogs - adopted_weekly - adopted_monthly  
    result = remaining_dogs
    return result

print(solution())