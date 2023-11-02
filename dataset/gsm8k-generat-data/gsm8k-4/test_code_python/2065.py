def solution():
    """Myrtle’s 3 hens lay 3 eggs a day. She would be gone for 7 days and told her neighbor to take as many as they would like. The neighbor took 12 eggs. Once home, Myrtle collected the remaining eggs, dropping 5 on the way into her house. How many eggs does Myrtle have?"""
    # Calculate the total number of eggs laid during the 7 days Myrtle was gone
    total_eggs = 3 * 3 * 7

    # Subtract the 12 eggs taken by the neighbor
    total_eggs -= 12

    # Subtract the 5 eggs that Myrtle dropped on the way into her house
    total_eggs -= 5

    # Display the total number of eggs that Myrtle has
    result = total_eggs
    return result

print(solution())