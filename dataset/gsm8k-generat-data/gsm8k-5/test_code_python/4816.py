def solution():
    total_chicken = 11  # Mrs. Crocker made 11 pieces of fried chicken
    lyndee_chicken = 1  # Lyndee ate 1 piece of chicken
    friends_chicken = total_chicken - lyndee_chicken  # Friends ate the remaining chicken

    # Calculate the number of friends based on the number of chicken pieces they ate
    num_friends = friends_chicken // 2
    result = num_friends
    return result

print(solution())