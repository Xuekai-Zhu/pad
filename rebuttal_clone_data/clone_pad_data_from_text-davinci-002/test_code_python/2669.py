def solution():
     in_person_tvs = 8
     online_store_tvs = 3 * in_person_tvs
     total_tvs = in_person_tvs + online_store_tvs
     auction_site_tvs = total_tvs - online_store_tvs
     result = auction_site_tvs
     return result

print(solution())