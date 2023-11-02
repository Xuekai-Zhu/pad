def solution():
    """The marching band is ordering new uniforms. Each uniform comes with a hat that costs $25, a jacket that costs three times as much as the hat, and pants that cost the average of the costs of the hat and jacket. How much does each uniform cost total?"""
    hat_cost = 25
    jacket_cost = hat_cost * 3
    pants_cost = (hat_cost + jacket_cost) / 2
    total_cost = hat_cost + jacket_cost + pants_cost
    result = total_cost
    return result

print(solution())