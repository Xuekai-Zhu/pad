def solution():
    # Calculate the number of seashells picked on Tuesday
    monday_seashells = 30
    tuesday_seashells = monday_seashells / 2

    # Calculate the total number of seashells picked
    total_seashells = monday_seashells + tuesday_seashells

    # Calculate the total amount of money Sally can make
    seashell_price = 1.20
    total_money = total_seashells * seashell_price

    result = total_money
    return result

print(solution())