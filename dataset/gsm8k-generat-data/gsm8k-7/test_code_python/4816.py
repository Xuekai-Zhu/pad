def solution():
    total_chicken = 11
    lyndee_chicken = 1
    friends_chicken = 2

    # Calculate the total number of chicken pieces eaten by Lyndee's friends
    friends_total_chicken = total_chicken - lyndee_chicken

    # Calculate the number of friends Lyndee had over
    num_friends = friends_total_chicken // friends_chicken
    result = num_friends
    return result

print(solution())