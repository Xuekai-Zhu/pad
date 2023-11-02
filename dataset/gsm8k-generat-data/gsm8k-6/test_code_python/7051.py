def solution():
    # Calculate the number of people who will win a prize
    num_winners = int(800 * 0.15) 

    # Calculate the total number of minnows that will be used as prizes
    num_prizes = num_winners * 3

    # Calculate the number of minnows left over
    num_leftover = 600 - num_prizes
    result = num_leftover
    return result

print(solution())