def solution():
    """In the matrix, there are seven fewer noodles than pirates. If there are 45 pirates, how many noodles and pirates are there in total?"""
    # Define the number of pirates
    pirates = 45

    # Calculate the number of noodles
    noodles = pirates - 7

    # Calculate the total number of pirates and noodles
    total = pirates + noodles

    # Return the result as a tuple
    result = (total, noodles, pirates)
    return result

print(solution())