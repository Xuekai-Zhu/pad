def solution():
    nylon_per_dog_collar = 18  # 18 inches of nylon per dog collar
    nylon_per_cat_collar = 10  # 10 inches of nylon per cat collar
    num_dog_collars = 9  # Janet needs to make 9 dog collars
    num_cat_collars = 3  # Janet needs to make 3 cat collars

    # Calculate the total amount of nylon needed for the dog collars
    total_nylon_dog = nylon_per_dog_collar * num_dog_collars

    # Calculate the total amount of nylon needed for the cat collars
    total_nylon_cat = nylon_per_cat_collar * num_cat_collars

    # Calculate the total amount of nylon needed
    total_nylon = total_nylon_dog + total_nylon_cat
    result = total_nylon
    return result

print(solution())