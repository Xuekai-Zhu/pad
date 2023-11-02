def solution():
    beef = 4  # John buys 4 pounds of beef
    beef_used = beef - 1  # John uses all but 1 pound of beef in soup
    veggies_used = 2 * beef_used  # John uses twice as many pounds of veggies as beef

    result = veggies_used
    return result

print(solution())