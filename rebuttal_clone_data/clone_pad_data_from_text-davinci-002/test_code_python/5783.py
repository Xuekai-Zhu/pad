def solution():
    josiah_days = 24
    josiah_quarters = josiah_days * .25
    leah_days = 20
    leah_cents = leah_days * .50
    megan_days = 12
    megan_cents = leah_cents * 2
    total_cents = josiah_quarters + leah_cents + megan_cents
    result = total_cents
    return result

print(solution())