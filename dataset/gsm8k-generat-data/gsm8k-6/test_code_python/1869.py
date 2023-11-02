def solution():
    # Calculate the total amount of money Francie received
    total_money = (5 * 8) + (6 * 6)  # $5 a week for 8 weeks, then $6 a week for 6 weeks

    # Calculate how much money Francie used to buy new clothes
    clothes_money = total_money / 2  

    # Calculate how much money Francie had left after buying the video game
    remaining_money = total_money - clothes_money - 35

    result = remaining_money
    return result

print(solution())