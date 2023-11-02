def solution():
    # Calculate the total amount spent by Randy in a year
    total_spent = 2 * 4 * 12  # Randy spends 2 dollars every time he goes to the store, and he makes 4 trips every month, so he spends 2*4=8 dollars each month. In a year, he spends 8*12=96 dollars.

    # Calculate the initial amount of money Randy had in his piggy bank
    initial_amount = total_spent + 104  # Randy had $104 left in his piggy bank after a year, so initially he had 104 + 96 = 200 dollars
    result = initial_amount
    return result

print(solution())