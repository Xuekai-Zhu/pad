def solution():
    # Calculate the number of additional cans Jennifer bought for every 5 cans Mark bought
    additional_cans = 6 

    # Calculate the number of cans Jennifer bought before meeting Mark
    jennifer_cans = 40 

    # Calculate the number of additional cans Jennifer bought after meeting Mark
    mark_cans = 50 
    additional_jennifer_cans = (mark_cans / 5) * additional_cans 

    # Calculate the total number of cans Jennifer bought
    total_jennifer_cans = jennifer_cans + additional_jennifer_cans 
    result = total_jennifer_cans
    return result

print(solution())