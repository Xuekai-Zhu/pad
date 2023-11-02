def solution():
    time_on_outreach = 4
    time_on_advertisement = time_on_outreach / 2
    total_time = 8
    time_on_marketing = total_time - time_on_outreach - time_on_advertisement
    result = time_on_marketing
    return result

print(solution())