def solution():
    """Hanna has $300. She wants to buy roses at $2 each and give some of the roses to her friends, Jenna and Imma. Jenna will receive  1/3 of the roses, and  Imma will receive 1/2 of the roses. How many roses does Hanna give to her friends?"""
    # Define the price of each rose and the amount of money Hanna has
    rose_price = 2
    hanna_money = 300

    # Calculate the maximum number of roses Hanna can buy
    max_roses = hanna_money // rose_price

    # Calculate the number of roses Jenna will receive
    jenna_roses = max_roses // 3

    # Calculate the number of roses Imma will receive
    imma_roses = max_roses // 2

    # Calculate the total number of roses Hanna will give to her friends
    total_roses = jenna_roses + imma_roses

    result = total_roses
    return result

print(solution())