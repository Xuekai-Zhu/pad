def solution():
    """Janet has a business selling custom collars for dogs and cats. If it takes 18 inches of nylon to make a dog collar and 10 inches to make a cat collar, how much nylon does she need to make 9 dog collars and 3 cat collars?"""
    # Define the amount of nylon needed for each type of collar
    DOG_COLLAR_NYLON = 18
    CAT_COLLAR_NYLON = 10

    # Define the number of dog and cat collars
    num_dog_collar = 9
    num_cat_collar = 3

    # Calculate the total amount of nylon needed
    total_nylon = (DOG_COLLAR_NYLON * num_dog_collar) + (CAT_COLLAR_NYLON * num_cat_collar)

    # Display the total amount of nylon needed
    result = total_nylon
    return result

print(solution())