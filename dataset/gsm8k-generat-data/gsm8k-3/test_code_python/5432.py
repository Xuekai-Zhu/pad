def solution():
    """What is the average age of the 1st and 5th fastest dogs if the 1st fastest dog is 10 years old, the 2nd fastest dog is 2 years younger than the first fastest dog, the 3rd fastest dog is 4 years older than the 2nd fastest dog, the 4th fastest dog is half the age of the 3rd fastest dog, and the 5th fastest dog is 20 years older than the 4th fastest dog?"""
    # Define the ages of each dog
    dog1_age = 10
    dog2_age = dog1_age - 2
    dog3_age = dog2_age + 4
    dog4_age = dog3_age / 2
    dog5_age = dog4_age + 20

    # Calculate the average age of the 1st and 5th fastest dogs
    avg_age = (dog1_age + dog5_age) / 2

    # Display the average age
    result = avg_age
    return result

print(solution())