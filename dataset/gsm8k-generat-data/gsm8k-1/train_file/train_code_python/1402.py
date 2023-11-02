def solution():
    """Brad’s zip code consists of five numbers that add up to 10. The first and second numbers are the same.
    The third number is zero. The fourth number is double the first number. The fourth and fifth numbers add up to 8. 
    What is Brad’s zip code?"""
    
    # set up equations based on given information
    # let x be the first and second numbers
    # let y be the fourth number
    # using the fact that the sum is 10: x + x + 0 + y + (8-y) = 10 
    # using the fact that the fourth and fifth numbers add up to 8: y + (8-y) = 8
    
    x = None
    y = None
    
    # solve the system of equations
    for i in range(1, 5):
        for j in range(i, 6):
            if i == j:
                # x and y are equal
                x = (10 - i - 0 - j - (8-j)) / 2
                y = j
            elif i == 1 and j == 4:
                # y is double x
                x = (10 - i - 0 - j - (8-j)) / 3
                y = 2 * x
            elif j == 5:
                # y + 8 - y = 8
                x = (10 - i - 0 - j - (8-j)) / 2
                y = j
    
    # construct the zip code string
    zip_code = str(int(x)) + str(int(x)) + "0" + str(int(y)) + str(int(8-y))
    
    return zip_code

print(solution())