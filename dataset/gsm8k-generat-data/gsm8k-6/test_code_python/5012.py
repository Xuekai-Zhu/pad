def solution():
    # Calculate the number of sweater vests that Carlton owns
    num_vests = 2 * 3  # Carlton has twice as many sweater vests as button-up shirts (3)

    # Calculate the total number of outfits Carlton can create
    num_outfits = num_vests * 3  # Carlton can pair each of his 3 button-up shirts with one of his num_vests sweater vests

    result = num_outfits
    return result

print(solution())