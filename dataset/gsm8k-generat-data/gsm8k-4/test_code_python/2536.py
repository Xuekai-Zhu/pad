def solution():
    """To earn money for her new computer, Tina sells handmade postcards. In a day, she can make 30 such postcards. For each postcard sold, Tina gets $5. How much money did Tina earn if she managed to sell all the postcards she made every day for 6 days?"""
    # Define the number of postcards Tina can make in a day and the number of days she sold postcards
    POSTCARDS_PER_DAY = 30
    DAYS = 6

    # Calculate the total number of postcards Tina made
    total_postcards = POSTCARDS_PER_DAY * DAYS

    # Calculate the total amount of money Tina earned
    total_money = total_postcards * 5

    result = total_money
    return result

print(solution())