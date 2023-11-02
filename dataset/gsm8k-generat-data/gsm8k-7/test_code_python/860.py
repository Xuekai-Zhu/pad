def solution():
    earl_money = 90
    fred_money = 48
    greg_money = 36

    earl_owes_fred = 28
    fred_owes_greg = 32
    greg_owes_earl = 40

    # Calculate the total amount of money exchanged
    total_money_exchanged = earl_owes_fred + fred_owes_greg + greg_owes_earl

    # Calculate the net loss or gain of each person
    earl_net = earl_money - earl_owes_fred + greg_owes_earl
    fred_net = fred_money + earl_owes_fred - fred_owes_greg
    greg_net = greg_money + fred_owes_greg - greg_owes_earl

    # Calculate the total money that Earl and Greg will have together after all debts are paid
    total_money_eg = earl_net + greg_net
    result = total_money_eg
    return result

print(solution())