def solution():
    """Elizabeth, Emma, and Elsa went shopping on Wednesday. In total Emma spent $58 If Elsa spent twice as much as Emma, and Elizabeth spent four times as much as Elsa, how much money did they spend in total?"""
    # Define the amount Emma spent
    emma_spent = 58

    # Calculate the amount Elsa spent
    elsa_spent = 2 * emma_spent

    # Calculate the amount Elizabeth spent
    elizabeth_spent = 4 * elsa_spent

    # Calculate the total amount they spent
    total_spent = emma_spent + elsa_spent + elizabeth_spent

    # Display the total amount they spent
    result = total_spent
    return result

print(solution())