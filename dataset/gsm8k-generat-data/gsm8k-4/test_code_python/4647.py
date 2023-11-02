def solution():
    """Monica was saving money for her future. Every week he put $15 into her moneybox. After the moneybox got full, which took 60 weeks, Monica took all the money out and took it to the bank, and she started saving money again. She repeated this whole process 5 times. How much money did Monica take to the bank in total?"""
    # Define the amount of money Monica saves each week
    weekly_savings = 15

    # Define the number of weeks it takes to fill up the moneybox
    weeks_to_fill_box = 60

    # Calculate the total amount of money Monica saves each time she fills up the moneybox
    box_total = weekly_savings * weeks_to_fill_box

    # Calculate the total amount of money Monica takes to the bank after 5 cycles
    total_bank_savings = box_total * 5

    result = total_bank_savings
    return result

print(solution())