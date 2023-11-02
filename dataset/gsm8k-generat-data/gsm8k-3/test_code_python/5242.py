def solution():
    """Willy has 10 stuffed animals. His mom gives him 2 more stuffed animals for his birthday. After his birthday, if his dad gives him 3 times more stuffed animals than he has, how many stuffed animals does Willy have in total?"""
    # Define the initial number of stuffed animals
    initial_count = 10

    # Add the number of stuffed animals Willy receives from his mom
    mom_gift = 2
    count = initial_count + mom_gift

    # Add the number of stuffed animals Willy receives from his dad
    dad_gift = count * 3
    total_count = count + dad_gift

    # Display the total number of stuffed animals
    result = total_count
    return result

print(solution())