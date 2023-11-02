def solution():
    # Calculate the amount spent by Heaven
    heaven_spent = 2*5 + 4*5  # Heaven bought 2 sharpeners and 4 notebooks at $5 each

    # Calculate the amount spent by Heaven's brother on erasers
    brother_spent = 100 - heaven_spent  # Heaven and her brother were given $100 in total and Heaven spent $heaven_spent
    erasers_spent = 10*4  # Heaven's brother bought 10 erasers at $4 each

    # Calculate the amount spent by Heaven's brother on highlighters
    highlighters_spent = brother_spent - erasers_spent
    result = highlighters_spent
    return result

print(solution())