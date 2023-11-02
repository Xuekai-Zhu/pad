def solution():
    cans_at_home = 12  # Collin found 12 cans at home
    cans_at_grandparents = 3 * cans_at_home  # Collin found three times as many cans at his grandparents' house
    cans_from_neighbor = 46  # Collin's neighbor gave him 46 cans
    cans_from_dad = 250  # Collin's dad brought home 250 cans from the office
    total_cans = cans_at_home + cans_at_grandparents + cans_from_neighbor + cans_from_dad  # Calculate the total number of cans

    # Calculate the total amount of money Collin can earn
    total_money = total_cans * 0.25

    # Calculate the amount of money Collin needs to put into savings
    savings_amount = total_money * 0.5
    result = savings_amount
    return result

print(solution())