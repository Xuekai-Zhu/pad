def solution():
    mb_downloaded = 310
    mb_to_download = 880
    download_rate = 3
    time_remaining = (mb_to_download - mb_downloaded) / download_rate
    result = time_remaining
    return result

print(solution())