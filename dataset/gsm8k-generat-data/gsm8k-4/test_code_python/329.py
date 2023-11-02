def solution():
    """Samuel bought 2 dozen doughnuts and Cathy bought 3 dozen doughnuts. They planned to share the doughnuts evenly with their 8 other friends. How many doughnuts will each of them receive?"""
    # Define the number of dozens of doughnuts Samuel and Cathy bought
    samuel_dozens = 2
    cathy_dozens = 3

    # Calculate the total number of doughnuts
    total_doughnuts = (samuel_dozens + cathy_dozens) * 12

    # Divide the doughnuts evenly among their 8 friends
    doughnuts_per_person = total_doughnuts / 8

    # Return the result
    result = doughnuts_per_person
    return result

print(solution())