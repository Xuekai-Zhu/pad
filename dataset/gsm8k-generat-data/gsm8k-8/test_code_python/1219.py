def solution():
    # Define the number of each order
    num_fried_chicken = 2
    num_chicken_pasta = 6
    num_bbq_chicken = 3

    # Calculate the total number of pieces of chicken needed
    total_chicken = num_fried_chicken*8 + num_chicken_pasta*2 + num_bbq_chicken*3

    result = total_chicken
    return result

print(solution())