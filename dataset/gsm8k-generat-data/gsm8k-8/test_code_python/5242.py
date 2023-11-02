def solution():
    # Define initial number of stuffed animals
    initial = 10

    # Add 2 more for Willy's birthday present
    after_birthday = initial + 2

    # Calculate how many more his dad gives him (3 times the initial amount)
    dad_gift = 3 * initial

    # Calculate the total number of stuffed animals Willy has
    total = after_birthday + dad_gift
    result = total
    return result

print(solution())