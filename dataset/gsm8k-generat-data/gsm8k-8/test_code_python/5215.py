def solution():
    # Calculate the number of hairs that Anya loses when she washes her hair
    hairs_lost_washing = 32

    # Calculate the number of hairs that Anya brushes out
    hairs_lost_brushing = 0.5 * hairs_lost_washing

    # Calculate the total number of hairs lost each time she washes and brushes her hair
    total_hairs_lost_per_cycle = hairs_lost_washing + hairs_lost_brushing

    # Calculate the number of hairs Anya needs to grow back each cycle to always have one more hair than she started with
    hairs_to_regrow_per_cycle = total_hairs_lost_per_cycle + 1

    result = hairs_to_regrow_per_cycle
    return result

print(solution())