def solution():
    gnomes_in_westerville = 20  # There are 20 gnomes in Westerville woods
    gnomes_in_ravenswood = 4 * gnomes_in_westerville  # Ravenswood has four times as many gnomes as Westerville
    percentage_to_take = 40  # 40% of the gnomes will be taken by the forest owner

    # Calculate the number of gnomes taken by the forest owner from Ravenswood forest
    gnomes_to_take = round(percentage_to_take / 100 * gnomes_in_ravenswood)
    
    # Calculate the number of gnomes remaining in Ravenswood forest
    gnomes_remaining = gnomes_in_ravenswood - gnomes_to_take
    result = gnomes_remaining
    return result

print(solution())