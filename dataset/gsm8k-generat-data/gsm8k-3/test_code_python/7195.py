def solution():
    """Dorchester works at a puppy wash. He is paid $40 per day + $2.25 for each puppy he washes. On Wednesday, Dorchester earned $76. How many puppies did he wash that day?"""
    # Define Dorchester's base pay and pay per puppy
    BASE_PAY = 40
    PAY_PER_PUPPY = 2.25

    # Define Dorchester's earnings
    earnings = 76

    # Calculate the number of puppies Dorchester washed
    puppies_washed = (earnings - BASE_PAY) / PAY_PER_PUPPY

    # Display the number of puppies washed
    result = puppies_washed
    return result

print(solution())