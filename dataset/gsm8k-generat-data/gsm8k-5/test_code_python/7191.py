def solution():
    monday_seashells = 30  # Sally picks 30 seashells on Monday
    tuesday_seashells = monday_seashells / 2  # Sally picks half as many seashells on Tuesday
    total_seashells = monday_seashells + tuesday_seashells  # Sally has a total of seashells to sell
    seashell_price = 1.20  # Sally can sell each seashell for $1.20

    # Calculate the total amount of money Sally can make
    total_money = total_seashells * seashell_price
    result = total_money
    return result

print(solution())