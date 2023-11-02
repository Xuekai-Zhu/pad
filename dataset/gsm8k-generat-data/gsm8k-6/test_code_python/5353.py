def solution():
    # Set up the equations to solve for the number of kittens
    # 2P + K*15 = 100  (where P is the number of puppies and K is the number of kittens)
    # K = (100 - 2P)/15
    
    # Test values for P from 0 to 10 and find the value that gives a whole number solution for K
    for P in range(11):
        K = (100 - 2*P)/15
        if K == int(K):  # check if K is a whole number
            result = int(K)
            return result

print(solution())