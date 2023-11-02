def solution():
    """Sally Draper gave her dad Don Draper 10oz of rum on his pancakes. Don can consume a maximum of 3 times that amount of rum for a healthy diet. If he already had 12oz of rum earlier that day, how many oz of rum can Don have after eating all of the rum and pancakes?"""
    rum_on_pancakes = 10
    max_rum_daily = rum_on_pancakes * 3
    consumed_rum = rum_on_pancakes + 12
    remaining_rum = max_rum_daily - consumed_rum
    result = remaining_rum
    return result

print(solution())