def solution():
    """Bobby wanted pancakes for breakfast. The recipe on the box makes 21 pancakes. While he ate 5 pancakes, his dog jumped up and was able to eat 7 before being caught. How many pancakes does Bobby have left?"""
    total_pancakes = 21
    bobby_ate = 5
    dog_ate = 7
    remaining_pancakes = total_pancakes - bobby_ate - dog_ate
    result = remaining_pancakes
    return result

print(solution())