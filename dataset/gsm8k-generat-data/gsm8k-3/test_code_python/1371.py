def solution():
    """Natalie's father has saved up $10,000 to split up between his kids.  Natalie will get half, as she is the oldest.  Rick will get 60 percent of the remaining money, and Lucy will get whatever is left after Natilie and Rick get paid.  How much money does Lucy get?"""
    # Define the initial amount saved
    total_money = 10000

    # Calculate Natalie's share
    natalie_share = total_money / 2

    # Calculate the remaining money after Natalie's share
    remaining_money = total_money - natalie_share

    # Calculate Rick's share
    rick_share = remaining_money * 0.6

    # Calculate Lucy's share
    lucy_share = total_money - natalie_share - rick_share

    # Display Lucy's share
    result = lucy_share
    return result

print(solution())