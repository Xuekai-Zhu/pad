def solution():
    # Calculate the total number of weeds pulled up by Sarah
    weeds_on_Tuesday = 25
    weeds_on_Wednesday = 3 * weeds_on_Tuesday
    weeds_on_Thursday = int(1/5 * weeds_on_Wednesday)
    weeds_on_Friday = weeds_on_Thursday - 10
    total_weeds = weeds_on_Tuesday + weeds_on_Wednesday + weeds_on_Thursday + weeds_on_Friday
    result = total_weeds
    return result

print(solution())