def solution():
    dog_collar_length = 18
    cat_collar_length = 10
    num_dog_collars = 9
    num_cat_collars = 3

    # Calculate the total length of nylon needed for dog collars
    total_dog_collar_length = dog_collar_length * num_dog_collars

    # Calculate the total length of nylon needed for cat collars
    total_cat_collar_length = cat_collar_length * num_cat_collars

    # Calculate the total length of nylon needed for all collars
    total_nylon_length = total_dog_collar_length + total_cat_collar_length
    result = total_nylon_length
    return result

print(solution())