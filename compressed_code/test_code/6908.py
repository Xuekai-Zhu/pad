def solution():
    
    initial_dogs = 200
    incoming_dogs = 100
    given_for_adoption = 40
    adopted_dogs = 60
    total_dogs = initial_dogs + incoming_dogs - given_for_adoption - adopted_dogs
    result = total_dogs
    return result

print(solution())