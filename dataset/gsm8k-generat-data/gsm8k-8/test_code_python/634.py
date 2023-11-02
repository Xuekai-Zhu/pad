def solution():
    # Calculate the total number of stripes on the hats with three stripes
    stripes_on_3_stripe_hats = 4 * 3

    # Calculate the total number of stripes on the hats with four stripes
    stripes_on_4_stripe_hats = 3 * 4

    # Calculate the total number of stripes on the hats with no stripes
    stripes_on_no_stripe_hats = 6 * 0

    # Calculate the total number of stripes on the hats with 5 stripes
    stripes_on_5_stripe_hats = 2 * 5

    # Calculate the combined total number of stripes on all of Vaishali's hats
    total_stripes = stripes_on_3_stripe_hats + stripes_on_4_stripe_hats + stripes_on_no_stripe_hats + stripes_on_5_stripe_hats
    result = total_stripes
    return result

print(solution())