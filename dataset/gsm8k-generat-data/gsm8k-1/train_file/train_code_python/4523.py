def solution():
    """Johann had 60 oranges. He decided to eat 10. Once he ate them, half were stolen by Carson. Carson returned exactly 5. How many oranges does Johann have now?"""
    initial_oranges = 60
    eaten_oranges = 10
    remaining_oranges = initial_oranges - eaten_oranges
    stolen_oranges = remaining_oranges / 2
    returned_oranges = 5
    final_oranges = remaining_oranges - stolen_oranges + returned_oranges
    result = final_oranges
    return result

print(solution())