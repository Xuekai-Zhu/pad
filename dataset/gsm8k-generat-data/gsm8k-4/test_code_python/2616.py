def solution():
    """Don buys recyclable bottles in a small town. Shop A normally sells him 150 bottles, shop B sells him 180 bottles and Shop C sells him the rest. How many bottles does Don buy from Shop C if he is capable of buying only 550 bottles?"""
    # Define the number of bottles sold by Shop A and Shop B
    bottles_A = 150
    bottles_B = 180

    # Define the total number of bottles Don can buy
    total_bottles = 550

    # Calculate the number of bottles Don can buy from Shop C
    bottles_C = total_bottles - (bottles_A + bottles_B)

    result = bottles_C
    return result

print(solution())