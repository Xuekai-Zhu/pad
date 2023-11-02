def solution():
    """The school store had a sale on pencils. Ten students bought pencils. 
    The first two students bought 2 pencils each. The next six students bought 
    three pencils each and the last two students only bought one pencil each. 
    How many pencils were sold?"""
    pencils_bought = 0
    pencils_bought += 2 * 2  # first two students bought 2 pencils each
    pencils_bought += 6 * 3  # next six students bought 3 pencils each
    pencils_bought += 2 * 1  # last two students bought 1 pencil each
    result = pencils_bought
    return result

print(solution())