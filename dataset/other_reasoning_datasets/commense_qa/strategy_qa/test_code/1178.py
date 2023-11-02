def solution():
    # Define the types of pancakes and coins
    pancake_types = ["silver dollar", "dollar", "half dollar"]
    coin_types = ["silver dollar", "dollar", "half dollar"]
    
    # Check if any pancake types are named after coins
    if set(pancake_types).intersection(coin_types):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())