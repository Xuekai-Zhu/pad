def solution():
    initial_money = 12  # Cathy initially had $12
    dad_money = 25  # Cathy's dad sent her $25
    mom_money = 2 * dad_money  # Cathy's mom sent her twice the amount her dad sent her

    # Add up all the money Cathy has now
    total_money = initial_money + dad_money + mom_money
    result = total_money
    return result

print(solution())