def solution():
    """Chad has 100 apples and each apple has different sizes and different price ranges. Each small apple cost $1.5, medium apple cost $2, and big apples cost $3. If Donny bought 6 small and medium apples and also 8 big apples, how much will Donny have to pay for all of it?"""
    small_apple_cost = 1.5
    medium_apple_cost = 2
    big_apple_cost = 3
    small_and_medium_apples = 6
    big_apples = 8
    total_cost = (small_and_medium_apples * (small_apple_cost + medium_apple_cost)) + (big_apples * big_apple_cost)
    result = total_cost
    return result

print(solution())