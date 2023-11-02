def solution():
    """George is about to celebrate his 25th birthday. Since his 15th birthday, he's been given a special $1 bill from his parents. They told him that on his 25th birthday, for every bill he still has, they will give him $1.5 in exchange. He spent 20% of his special bills. How much will he receive from his parents when he exchanges them?"""
    starting_bills = 10  # George gets 1 bill every year from age 15 to 25
    spent_bills = int(starting_bills * 0.2)  # 20% of bills spent
    remaining_bills = starting_bills - spent_bills
    exchange_rate = 1.5
    total_exchange = remaining_bills * exchange_rate
    result = total_exchange
    return result

print(solution())