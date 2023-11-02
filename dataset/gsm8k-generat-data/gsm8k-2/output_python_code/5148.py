def solution():
    """Danny has a huge fish tank that contains 94 guppies, 76 angelfish, 89 tiger sharks, and 58 Oscar fish. If he sells 30 guppies, 48 angelfish, 17 tiger sharks, and 24 Oscar fish. How many fish will remain?"""
    initial_total_fish = 94 + 76 + 89 + 58
    sold_fish = 30 + 48 + 17 + 24
    remaining_fish = initial_total_fish - sold_fish
    result = remaining_fish
    return result

print(solution())