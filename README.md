# GeoJson

GeoJson from Brazilian states.

The official source (IBGE) provides only the area code (numerical identifier) 
and in some applications we need additional information (such as name and state abbreviation). 
This  script was created to request IBGE and update GeoJson properties with the necessary 
additional information (based on mapping.json).

## Applications using this repo:
- Metabase: the metabase expects a URL that contains the raw json file containing the label that will be shown in the view (state name)
  and the identifier field that will be used to map the query (status acronym).


## Update:
To update GeoJson just run the following command:

```commandline
    python update_geojson_file.py 
```



