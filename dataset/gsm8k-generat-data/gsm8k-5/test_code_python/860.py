def solution():
    # Calculate how much Earl will have left after paying Fred and receiving from Greg
    earl = 90 - 28 + 40  # Earl owes $28 and receives $40
    # Calculate how much Fred will have left after receiving from Earl and paying Greg
    fred = 48 + 28 - 32  # Fred receives $28 from Earl and owes $32 to Greg
    # Calculate how much Greg will have left after receiving from Fred and paying Earl
    greg = 36 + 32 - 40  # Greg receives $32 from Fred and owes $40 to Earl
    # Calculate how much Greg and Earl will have together after all debts are paid
    total = earl + greg
    result = total
    return result

print(solution())