def solution():
    """On Saturday morning, Renata had $10 to spend. She first went and made a $4 donation in exchange for a ticket to the local charity draw. When the draw was done, she was declared the winner of the 5th prize of $90. Excited, she quickly dashed to play slots at one of the casinos in Atlantic City. Unfortunately, she lost $50 at the first slot machine, $10 at the second and $5 at the last one.  Dejected, she decided to take a long walk. She soon grew thirsty and entered the first gas station she saw. She picked a $1 bottle of water and while paying for it, she bought a $1 lottery ticket. To her utter delight, she won an instant prize of $65. How much money did Renata end up having?"""
    
    # Define the amount Renata started with
    starting_amount = 10

    # Make the $4 donation and get a ticket to the local charity draw
    starting_amount -= 4

    # Win the 5th prize of $90 in the charity draw
    starting_amount += 90

    # Lose $50 at the first slot machine, $10 at the second, and $5 at the last one
    starting_amount -= (50 + 10 + 5)

    # Buy a bottle of water for $1 at a gas station and a lottery ticket for $1
    starting_amount -= 2

    # Win an instant prize of $65 from the lottery ticket
    starting_amount += 65

    # Display the amount of money Renata ended up having
    result = starting_amount
    return result

print(solution())