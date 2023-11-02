def solution():
    """Sally Draper gave her dad Don Draper 10oz of rum on his pancakes. Don can consume a maximum of 3 times that amount of rum for a healthy diet. If he already had 12oz of rum earlier that day, how many oz of rum can Don have after eating all of the rum and pancakes?"""
    max_rum_consumption = 3 * 10
    total_rum_consumption = 10 + 12
    remaining_rum_consumption = max_rum_consumption - total_rum_consumption
    result = remaining_rum_consumption
    return result

print(solution())