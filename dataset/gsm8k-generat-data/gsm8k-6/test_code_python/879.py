def solution():
    # Calculate the number of bitcoins Jake has after each step
    bitcoins_after_donation = 80 - 20  # Jake donates 20 bitcoins to charity
    bitcoins_to_brother = bitcoins_after_donation / 2  # Jake gives half the bitcoins to his brother
    bitcoins_after_tripling = bitcoins_to_brother * 3  # Jake triples the number of bitcoins he has
    bitcoins_after_second_donation = bitcoins_after_tripling - 10  # Jake donates another 10 coins

    result = bitcoins_after_second_donation
    return result

print(solution())