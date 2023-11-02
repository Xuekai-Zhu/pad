def solution():
    # Work done by 1 builder in 1 day
    work_per_day = 1 / 30

    # Payment per day for 1 builder
    payment_per_day = 100

    # Work required to build 1 house with 6 floors
    work_per_house = 6

    # Work required to build 5 houses with 6 floors each
    total_work = 5 * 6 * work_per_house

    # Number of builders required to complete the work in the given time
    num_builders = total_work/(6 * 30)

    # Total payment required to hire 6 builders for the given work
    total_payment = num_builders * 6 * payment_per_day
    result = total_payment
    return result

print(solution())