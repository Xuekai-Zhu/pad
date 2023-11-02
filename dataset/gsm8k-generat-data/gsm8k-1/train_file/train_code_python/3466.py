def solution():
    """George is about to celebrate his 25th birthday. Since his 15th birthday, he's been given a special $1 bill from his parents. They told him that on his 25th birthday, for every bill he still has, they will give him $1.5 in exchange. He spent 20% of his special bills. How much will he receive from his parents when he exchanges them?"""
    starting_bills = 10  # he received one bill per year from age 15 to 24
    percent_spent = 20
    remaining_bills = starting_bills - (starting_bills * (percent_spent / 100))
    exchange_rate = 1.5
    amount_received = remaining_bills * exchange_rate
    result = amount_received
    return result

print(solution())