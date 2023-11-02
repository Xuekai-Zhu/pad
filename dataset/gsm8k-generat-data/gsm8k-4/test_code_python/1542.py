def solution():
    """Janet has a business selling custom collars for dogs and cats. If it takes 18 inches of nylon to make a dog collar and 10 inches to make a cat collar, how much nylon does she need to make 9 dog collars and 3 cat collars ?"""
    # Define the number of inches of nylon needed for a dog collar and a cat collar
    DOG_NYLON = 18
    CAT_NYLON = 10

    # Calculate the total amount of nylon needed for the dog collars
    dog_nylon_total = DOG_NYLON * 9

    # Calculate the total amount of nylon needed for the cat collars
    cat_nylon_total = CAT_NYLON * 3

    # Calculate the total amount of nylon needed for all the collars
    total_nylon = dog_nylon_total + cat_nylon_total

    # return the result
    result = total_nylon
    return result

print(solution())