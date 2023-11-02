def solution():
    # Define the total hours spent on customer outreach and advertisement
    outreach_hours = 4
    ad_hours = 0.5 * outreach_hours

    # Calculate the total hours spent on marketing
    marketing_hours = 8 - outreach_hours - ad_hours
    result = marketing_hours
    return result

print(solution())