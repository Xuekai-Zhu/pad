def solution():
    # Define the initial number of gummy bears
    num_gummy_bears = 100

    # Calculate the number of candies Josh gives to his siblings
    num_candies_given = 3 * 10

    # Subtract the candies given to siblings from the total candies
    num_gummy_bears -= num_candies_given

    # Calculate the number of candies Josh gives to his friend
    num_candies_given = num_gummy_bears / 2

    # Subtract the candies given to the friend from the total candies
    num_gummy_bears -= num_candies_given

    # Subtract the candies Josh wants to eat from the total candies
    num_gummy_bears -= 16

    result = num_gummy_bears
    return result

print(solution())