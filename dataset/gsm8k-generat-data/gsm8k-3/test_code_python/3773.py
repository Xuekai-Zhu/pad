def solution():
    """A packet of candy sweets has 30 cherry-flavored sweets, 40 strawberry-flavored sweets, and 50 pineapple-flavored sweets.
    Aaron eats half of each of the flavored sweets and gives 5 cherry-flavored sweets to his friend.
    How many sweets are still in the packet of candy?"""
    
    # Find total sweets initially present
    total_sweets = 30 + 40 + 50
    
    # Aaron eats half of each flavored sweet, hence reduces the candy by half
    total_sweets = total_sweets / 2
    
    # Aaron gives 5 cherry-flavored sweets to his friend
    total_sweets -= 5
    
    # Display the number of sweets remaining
    result = total_sweets
    return result

print(solution())