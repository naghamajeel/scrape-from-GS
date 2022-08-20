import os
import sys
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd
 params = {
  "engine": "google_scholar_profiles",
  "mauthors": "keywords",
  "api_key": "private api key"
 }
 search = GoogleSearch(params)
   
 profile_results_data = []
 i=10
 profiles_is_present = True
 profile_results = search.get_dict()

 for i in range(100):
   profile_results = search.get_dict()

   for profile in profile_results.get("profiles", []):

            thumbnail = profile.get("thumbnail")
            name = profile.get("name".translate(non_bmp_map))
            link = profile.get("link")
            author_id = profile.get("author_id")
            email = profile.get("email")
            cited_by = profile.get("cited_by")
            interests = profile.get("interests")
            print(f'Currently extracting with {profile.get("author_id")} ID. plus {(i)}')
            profile_results_data.append({
                "thumbnail": thumbnail,
                "name": name,
                "link": link,
                "author_id": author_id,
                "email": email,
                "cited_by": cited_by,
                "interests": interests
            })
   pd2=pd.DataFrame(profile_results_data)
   pd2.to_csv("res.csv", encoding="utf-8")
   if "next" in profile_results.get("pagination", []):
       search.params_dict.update(dict(parse_qsl(urlsplit(profile_results.get("pagination").get("next")).query)))
       i=i+10
   else:
       profiles_is_present = False
 
 print("Results Saved.")











