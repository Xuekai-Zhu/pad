def solution():
    """Daisy is a poodle puppy who loves to play with her dog toys. She often loses them in various ways, and her owner needs to replace them. On Monday, Daisy played with 5 dog toys. On Tuesday, Daisy had 3 dog toys left after losing some, and her owner went to the store and got her 3 more. On Wednesday, all of Daisy's old and new dog toys were missing, so her owner went to the store and bought her 5 more. If Daisy's owner found all the lost dog toys, including the new dog toys, how many dog toys would Daisy have now?"""
    # Calculate the number of dog toys Daisy had on Tuesday
    toys_tuesday = 3 + 3

    # Calculate the number of dog toys Daisy had on Wednesday
    toys_wednesday = toys_tuesday + 5

    # Calculate the total number of dog toys Daisy has now
    total_toys = 5 + toys_tuesday + toys_wednesday

    # Display the total number of dog toys Daisy has now
    result = total_toys
    return result

print(solution())