def solution():
    # Define the age of the fastest dog
    fastest_dog_age = 10
    
    # Calculate the age of the second fastest dog
    second_dog_age = fastest_dog_age - 2
    
    # Calculate the age of the third fastest dog
    third_dog_age = second_dog_age + 4
    
    # Calculate the age of the fourth fastest dog
    fourth_dog_age = third_dog_age / 2
    
    # Calculate the age of the fifth fastest dog
    fifth_dog_age = fourth_dog_age + 20
    
    # Calculate the average age of the first and fifth fastest dogs
    average_age = (fastest_dog_age + fifth_dog_age) / 2
    result = average_age
    return result

print(solution())