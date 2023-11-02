def solution():
    """Mark has an egg farm. His farm supplies one store with 5 dozen eggs and another store with 30 eggs each day. How many eggs does he supply these two stores in a week?"""
    # Define the number of eggs supplied to the first store each day
    eggs_first_store = 5 * 12

    # Define the number of eggs supplied to the second store each day
    eggs_second_store = 30

    # Calculate the total number of eggs supplied in a week
    total_eggs = (eggs_first_store + eggs_second_store) * 7

    # return the result
    result = total_eggs
    return result

print(solution())