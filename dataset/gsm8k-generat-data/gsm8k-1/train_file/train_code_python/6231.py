def solution():
    """There are four times as many boys at Lulu's party as girls. Each boy paid twice the money that each girl paid to attend the party. If there are 40 boys at the party and each boy paid $50 to attend the party, calculate the total amount of money collected at the party."""
    boys_ratio = 4
    girls_ratio = 1
    total_ratio = boys_ratio + girls_ratio
    boys_count = 40
    boys_payment = 50
    girls_payment = boys_payment / 2
    girls_count = boys_count * (girls_ratio / boys_ratio)
    total_payment = (boys_count * boys_payment) + (girls_count * girls_payment)
    result = total_payment
    return result

print(solution())