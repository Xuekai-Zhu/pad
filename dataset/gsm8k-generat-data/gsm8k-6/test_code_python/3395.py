def solution():
    # Calculate the size of Russia relative to the United States
    canada_size = 1.5  # Canada is 1.5 times bigger than the US
    russia_size = canada_size * (4/3)  # Russia is 1/3 bigger than Canada
    relative_size = russia_size / 1  # calculate Russia's size relative to the US
    result = relative_size
    return result

print(solution())