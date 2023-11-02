def solution():
    # Define the number of dogs and their respective bone hauls
    num_dogs = 5
    dog1_bones = 3
    dog2_bones = dog1_bones - 1
    dog3_bones = dog2_bones * 2
    dog4_bones = 1
    dog5_bones = dog4_bones * 2

    # Calculate the total number of bones
    total_bones = dog1_bones + dog2_bones + dog3_bones + dog4_bones + dog5_bones

    result = total_bones
    return result

print(solution())