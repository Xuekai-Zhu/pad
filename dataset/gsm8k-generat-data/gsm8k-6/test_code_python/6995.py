def solution():
    # Let x be the number of chihuahuas Bill actually bought
    # Then the number of rats he bought is 6x
    # The total number of animals he thought he bought is x + 6x = 7x
    # But he actually bought 70 animals, so 7x = 70
    # Therefore x = 10, and he actually bought 10 chihuahuas and 60 rats
    num_rats = 6 * 10
    result = num_rats
    return result

print(solution())