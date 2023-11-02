def solution():
    """Shelby was having a movie party for her birthday. She and her mom made a dozen bags of buttered popcorn and 10 bags of caramel popcorn. Her brother Alan took 3 bags of buttered popcorn and 1 bag of caramel popcorn for his friends. How many bags of popcorn does Shelby have left for the party?"""
    buttered_popcorn = 12
    caramel_popcorn = 10
    alan_buttered_popcorn = 3
    alan_caramel_popcorn = 1
    total_popcorn = buttered_popcorn + caramel_popcorn
    alan_popcorn = alan_buttered_popcorn + alan_caramel_popcorn
    remaining_popcorn = total_popcorn - alan_popcorn
    result = remaining_popcorn
    return result

print(solution())