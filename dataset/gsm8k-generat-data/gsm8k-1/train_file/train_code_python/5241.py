def solution():
    """Willy has 10 stuffed animals. His mom gives him 2 more stuffed animals for his birthday. After his birthday, if his dad gives him 3 times more stuffed animals than he has, how many stuffed animals does Willy have in total?"""
    initial_animals = 10
    mom_gift = 2
    total_animals = initial_animals + mom_gift
    dad_gift = total_animals * 3
    total_animals += dad_gift
    result = total_animals
    return result

print(solution())