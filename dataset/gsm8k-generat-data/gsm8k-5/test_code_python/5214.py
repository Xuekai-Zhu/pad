def solution():
    # Derek had 90/3 = 30 cars when he was 6 years old
    cars_6_years_old = 30

    # Ten years later, Derek sold some of his dogs and bought 210 more cars
    # Let's assume he sold x dogs and bought 210 cars, so he now has (90-x) dogs and (30+210) cars
    # The number of cars became twice the number of dogs, so we have 2(90-x) = 30+210+x
    # Solving for x, we get x = 60, so Derek now has (90-60)=30 dogs and (30+210)=240 cars
    dogs_now = 30
    result = dogs_now
    return result

print(solution())