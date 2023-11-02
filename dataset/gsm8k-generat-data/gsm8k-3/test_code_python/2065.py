def solution():
    """Myrtle’s 3 hens lay 3 eggs a day.  She would be gone for 7 days and told her neighbor to take as many as they would like.  The neighbor took 12 eggs.  Once home, Myrtle collected the remaining eggs, dropping 5 on the way into her house.  How many eggs does Myrtle have?"""
    # Define the number of hens and eggs they lay per day
    hens = 3
    eggs_per_day = 3

    # Calculate the total number of eggs laid while Myrtle was gone
    total_eggs = hens * eggs_per_day * 7

    # Subtract the eggs taken by the neighbor
    total_eggs -= 12

    # Subtract the eggs Myrtle dropped
    total_eggs -= 5

    # Display the remaining number of eggs
    result = total_eggs
    return result

print(solution())