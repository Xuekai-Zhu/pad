def solution():
    """Oliver collects trading cards. He has twice as many Monster Club cards as Alien Baseball cards. His Battle Gremlins card collection is the largest at 48 cards, three times the size of his Alien Baseball card collection. How many Monster Club cards does Oliver have?"""
    # Define the number of Battle Gremlins cards and Alien Baseball cards
    battle_gremlins = 48
    alien_baseball = battle_gremlins / 3

    # Calculate the number of Monster Club cards
    monster_club = 2 * alien_baseball

    # Return the result
    result = monster_club
    return result

print(solution())