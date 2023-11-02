def solution():
    """Oliver collects trading cards. He has twice as many Monster Club cards as Alien Baseball cards.
    His Battle Gremlins card collection is the largest at 48 cards, three times the size of his Alien Baseball card collection.
    How many Monster Club cards does Oliver have?"""
    battle_gremlins_cards = 48
    alien_baseball_cards = battle_gremlins_cards / 3
    monster_club_cards = 2 * alien_baseball_cards
    result = monster_club_cards
    return result

print(solution())