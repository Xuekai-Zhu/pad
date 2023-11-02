def solution():
    # Calculate the amount of money Lee can save in two months
    savings = 2 * 1000  

    # Calculate Lee's salary for two months
    salary = (60000/12) * 2  

    # Calculate the total amount of money Lee can spend on the ring
    total_money = savings + salary  

    # Calculate how many months it will take Lee to save enough money for the ring
    months_to_save = total_money / 2000  

    result = months_to_save
    return result

print(solution())