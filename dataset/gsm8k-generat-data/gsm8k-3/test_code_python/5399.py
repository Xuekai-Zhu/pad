def solution():
    """Steve's new book sells 1,000,000 copies.  He got an advance to pay for 100,000 copies. He gets $2 for each copy of the book sold.  His agent takes 10% of that.  How much money did he keep not counting the money from the advance?"""
    # Define the number of copies sold and the advance
    COPIES_SOLD = 1000000
    ADVANCE = 100000

    # Calculate Steve's earnings from the book sales
    earnings = (COPIES_SOLD - ADVANCE) * 2 * 0.9

    # Display Steve's earnings
    result = earnings
    return result

print(solution())