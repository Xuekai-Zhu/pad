def solution():
    total_pots = 80  # Cheyenne made 80 clay pots
    cracked_pots = 2/5 * total_pots  # 2/5 of the pots cracked
    usable_pots = total_pots - cracked_pots  # Calculate the number of usable pots

    # Calculate the total amount of money Cheyenne made from selling the usable pots
    total_money = usable_pots * 40
    result = total_money
    return result

print(solution())