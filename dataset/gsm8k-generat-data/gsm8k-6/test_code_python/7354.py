def solution():
    # Calculate the number of times Helen cuts her lawn each month
    cuts_per_month = [2, 2, 4, 4, 4, 4, 2, 2]  # March, April, May, June, July, August, September, October

    # Calculate the number of times Helen needs to refill her gas tank
    refills = sum(1 for i in range(len(cuts_per_month)) if (i+1) % 4 == 0)  # every 4th time she cuts her lawn

    # Calculate the total gallons of gas needed
    gallons_needed = refills * 2

    result = gallons_needed
    return result

print(solution())