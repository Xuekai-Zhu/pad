def solution():
    total_cupcakes = 60 # total cupcakes Anna baked
    given_away = (4/5) * total_cupcakes # cupcakes given away
    remaining = total_cupcakes - given_away # cupcakes remaining
    eaten = 3 # cupcakes eaten from the remaining
    left = remaining - eaten # cupcakes left
    result = left
    return result

print(solution())