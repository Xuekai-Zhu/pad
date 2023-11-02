def solution():
    # Calculate the number of cows Aaron has
    aaron_cows = 4 * 60

    # Calculate the total number of cows Aaron and Matthews have
    total_cows = aaron_cows + 60

    # Calculate the number of cows Marovich has
    marovich_cows = total_cows - 30

    # Calculate the total number of cows the three have
    total_cows_all = aaron_cows + 60 + marovich_cows
    result = total_cows_all
    return result

print(solution())