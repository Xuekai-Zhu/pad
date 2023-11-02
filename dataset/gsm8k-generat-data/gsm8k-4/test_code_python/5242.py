def solution():
    """Willy has 10 stuffed animals. His mom gives him 2 more stuffed animals for his birthday. After his birthday, if his dad gives him 3 times more stuffed animals than he has, how many stuffed animals does Willy have in total?"""
    # Define the initial number of stuffed animals
    initial_stuffed_animals = 10

    # Define the number of stuffed animals Willy gets for his birthday
    birthday_stuffed_animals = 2

    # Calculate the total number of stuffed animals after his birthday
    total_stuffed_animals = initial_stuffed_animals + birthday_stuffed_animals

    # Calculate the number of stuffed animals Willy gets from his dad
    dad_stuffed_animals = 3 * total_stuffed_animals

    # Calculate the total number of stuffed animals Willy has
    total_stuffed_animals += dad_stuffed_animals

    result = total_stuffed_animals
    return result

print(solution())