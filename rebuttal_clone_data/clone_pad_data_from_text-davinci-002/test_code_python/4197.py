def solution():
    sweaters = 28
    yarn_per_sweater = 4
    balls_of_yarn = sweaters * yarn_per_sweater
    cost_per_ball = 6
    cost_of_yarn = balls_of_yarn * cost_per_ball
    price_per_sweater = 35
    total_gain = sweaters * price_per_sweater - cost_of_yarn
    result = total_gain
    return result

print(solution())