def solution():
    # Define the number of pirates
    pirates = 45

    # Calculate the number of noodles based on the given relationship
    noodles = pirates - 7

    # Calculate the total number of pirates and noodles
    total = pirates + noodles

    result = (total, pirates, noodles)
    return result

print(solution())