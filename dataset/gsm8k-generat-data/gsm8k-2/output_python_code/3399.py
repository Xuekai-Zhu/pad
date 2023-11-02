def solution():
    """Rodney, Roger and Ron can lift a combined weight of 239 pounds. Rodney can lift twice as much as Roger, and Roger can lift 7 pounds less than 4 times the amount that Ron can lift. How much can Rodney lift?"""
    total_weight = 239
    ron_lift = 1  # We start at 1 to avoid division by 0.
    roger_lift = (ron_lift * 4) - 7
    rodney_lift = roger_lift * 2
    while rodney_lift + roger_lift + ron_lift != total_weight:
        ron_lift += 1
        roger_lift = (ron_lift * 4) - 7
        rodney_lift = roger_lift * 2
    result = rodney_lift
    return result

print(solution())