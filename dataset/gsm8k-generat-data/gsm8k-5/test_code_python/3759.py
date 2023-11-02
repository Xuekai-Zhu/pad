def solution():
    total_bottles = 180  # The van is delivering 180 bottles of drinks
    cider_bottles = 40  # 40 bottles contain only cider
    beer_bottles = 80  # 80 bottles contain only beer
    mixture_bottles = total_bottles - cider_bottles - beer_bottles  # The rest are a mixture of cider and beer
    half_bottles = (total_bottles - mixture_bottles) / 2  # Half of the non-mixture bottles will be given to the first house

    # Calculate the number of bottles from each category that will be given to the first house
    cider_to_first_house = half_bottles / 2
    beer_to_first_house = half_bottles / 2
    mixture_to_first_house = mixture_bottles / 2

    # Calculate the total number of bottles the first house will get
    total_to_first_house = cider_to_first_house + beer_to_first_house + mixture_to_first_house
    result = total_to_first_house
    return result

print(solution())