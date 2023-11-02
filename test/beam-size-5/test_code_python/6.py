def solution():
    # Calculate the number of downloads in the second month
    downloads_second_month = 3 * 60

    # Calculate the number of downloads in the third month
    downloads_third_month = 0.3 * 60

    # Calculate the total number of downloads over the three months
    total_downloads = 60 + downloads_second_month + downloads_third_month
    result = total_downloads
    return result

print(solution())