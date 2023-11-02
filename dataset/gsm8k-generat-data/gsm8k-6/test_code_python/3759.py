def solution():
    # Calculate the total number of bottles of mixture
    total_mixture = 180 - 40 - 80  # number of bottles that are a mixture of cider and beer

    # Calculate the number of bottles each drink type for the mixture
    cider_ratio = 2/5  # ratio of cider in the mixture
    beer_ratio = 3/5  # ratio of beer in the mixture
    mixture_cider = total_mixture * cider_ratio
    mixture_beer = total_mixture * beer_ratio

    # Calculate the number of bottles of each drink type for the first house
    first_house_cider = 40/2  # half of the bottles of cider
    first_house_beer = 80/2  # half of the bottles of beer
    first_house_mixture = total_mixture/2  # half of the bottles of mixture

    # Calculate the total number of bottles for the first house
    total_first_house = first_house_cider + first_house_beer + first_house_mixture

    result = total_first_house
    return result

print(solution())