def solution():
    """Rodney, Roger and Ron can lift a combined weight of 239 pounds. Rodney can lift twice as much as Roger, and Roger can lift 7 pounds less than 4 times the amount that Ron can lift. How much can Rodney lift?"""
    total_weight_lifted = 239
    ron_lifts = x
    roger_lifts = 4*ron_lifts - 7
    rodney_lifts = 2*roger_lifts

    combined_lifts = ron_lifts + roger_lifts + rodney_lifts
    ron_lifts = (total_weight_lifted - combined_lifts) / 3
    roger_lifts = 4 * ron_lifts - 7
    rodney_lifts = 2 * roger_lifts
    result = rodney_lifts

    return result

print(solution())