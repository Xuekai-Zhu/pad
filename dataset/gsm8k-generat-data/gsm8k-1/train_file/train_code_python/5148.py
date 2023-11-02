def solution():
    """Danny has a huge fish tank that contains 94 guppies, 76 angelfish, 89 tiger sharks, and 58 Oscar fish. If he sells 30 guppies, 48 angelfish, 17 tiger sharks, and 24 Oscar fish. How many fish will remain?"""
    initial_guppies = 94
    initial_angelfish = 76
    initial_tigersharks = 89
    initial_oscarfish = 58
    sold_guppies = 30
    sold_angelfish = 48
    sold_tigersharks = 17
    sold_oscarfish = 24
    remaining_guppies = initial_guppies - sold_guppies
    remaining_angelfish = initial_angelfish - sold_angelfish
    remaining_tigersharks = initial_tigersharks - sold_tigersharks
    remaining_oscarfish = initial_oscarfish - sold_oscarfish
    total_remaining_fish = remaining_guppies + remaining_angelfish + remaining_tigersharks + remaining_oscarfish
    result = total_remaining_fish
    return result

print(solution())