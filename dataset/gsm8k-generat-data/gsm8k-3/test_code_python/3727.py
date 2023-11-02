def solution():
    """Steph needs to cook fried chicken for the kid's party. She bought 24 pieces of drumstick and 4 fewer breast parts. How many fried chickens can Steph make?"""
    # Define the number of drumsticks and breasts purchased
    drumsticks = 24
    breasts = drumsticks - 4

    # Calculate the total number of fried chickens
    fried_chickens = (drumsticks + breasts) // 2

    # Display the total number of fried chickens
    result = fried_chickens
    return result

print(solution())