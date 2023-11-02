def solution():
    # Define the daily recommended sodium intake and the sodium content of two cans of Campbell's Soup
    daily_sodium_intake = 2300
    soup_sodium_content = 1400 # Assuming the lower end of the range for sodium content
    # Check if consuming two cans of Campbell's Soup exceeds the daily recommended sodium intake
    if soup_sodium_content * 2 > daily_sodium_intake:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())