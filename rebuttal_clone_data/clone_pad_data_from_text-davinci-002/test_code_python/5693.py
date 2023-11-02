def solution():
    sweaters_knit_Monday = 8
    sweaters_knit_Tuesday = sweaters_knit_Monday + 2
    sweaters_knit_Wednesday = sweaters_knit_Tuesday - 4
    sweaters_knit_Thursday = sweaters_knit_Wednesday - 4
    sweaters_knit_Friday = sweaters_knit_Monday / 2
    total_sweaters_knit = sweaters_knit_Monday + sweaters_knit_Tuesday + sweaters_knit_Wednesday + sweaters_knit_Thursday + sweaters_knit_Friday
    result = total_sweaters_knit
    return result

print(solution())