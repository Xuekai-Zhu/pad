def solution():
    """Daisy is a poodle puppy who loves to play with her dog toys. She often loses them, and her owner needs to replace them. On Monday, Daisy played with 5 dog toys. On Tuesday, Daisy had 3 dog toys left after losing some, and her owner went to the store and got her 3 more. On Wednesday, all of Daisy's old and new dog toys were missing, so her owner went to the store and bought her 5 more. If Daisy's owner found all the lost dog toys, including the new dog toys, how many dog toys would Daisy have now?"""
    # Define the initial number of dog toys
    dog_toys = 5

    # Add the 3 new dog toys bought on Tuesday
    dog_toys += 3

    # Add the 5 new dog toys bought on Wednesday
    dog_toys += 5

    # return the result
    result = dog_toys
    return result

print(solution())