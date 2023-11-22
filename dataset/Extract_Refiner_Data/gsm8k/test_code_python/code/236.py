def solution():
    
    # Let x be the number of candies Robert has
    # Then James has x + 6 candies
    # And John has twice as many candies as Robert, so he has 2x + 6 candies
    # And John has 54 candies, so he has 54 + 6 = 54
    # Solving for x, we get x = 26
    # Therefore, John has 26 candies and James has 26 candies

    john_candies = 26
    james_candies = john_candies - 6
    result = john_candies - james_candies
    return result

print(solution())