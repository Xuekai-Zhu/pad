def solution():
    eggs = 2 * 12  # Mark has two dozen eggs
    siblings = 3 + 1  # Mark has three siblings plus himself, for a total of four people
    eggs_per_person = eggs / siblings  # divide the eggs equally among the four people
    result = eggs_per_person
    return result

print(solution())