def solution():
    monday_seashells = 30
    tuesday_seashells = monday_seashells / 2
    price_per_seashell = 1.20

    # Calculate the total number of seashells Sally picked
    total_seashells = monday_seashells + tuesday_seashells

    # Calculate the total amount of money Sally can make by selling all her seashells
    total_money = total_seashells * price_per_seashell
    result = total_money
    return result

print(solution())