def solution():
    krabby_patty = {"patty": True, "bun": True, "lettuce": True, "onion": True, "tomato": True}
    cheeseburger = {"patty": True, "bun": True, "lettuce": True, "onion": True, "tomato": True, "cheese": True}
    # Check if a krabby patty is similar to a cheeseburger
    if krabby_patty == cheeseburger:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())