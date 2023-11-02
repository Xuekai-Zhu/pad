def solution():
    """Mary earns $20 washing cars and $40 walking dogs each month. If she puts half of that money away each month how long would it take her to save $150?"""
    # Define the amount earned from washing cars and walking dogs
    car_money = 20
    dog_money = 40

    # Determine the amount of money saved each month
    saved_money = (car_money + dog_money) * 0.5

    # Determine the number of months it will take to save $150
    months_to_save = 150 / saved_money

    result = int(months_to_save)
    return result

print(solution())