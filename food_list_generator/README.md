# Food Secretary -- Backend
The current food list data generator has to work with food_name.json. Can replace the json file with other json files as long as they follow the same format
The output of the food list data generator is a json file currently, working on uploading data directly to the database 

To generate a food list in the csv format and upload it to the data base, call the following functions:
1. Make sure `food_name.json` file is downloaded. Feel free to add more food into this file
2. Run `Foodlist_csvdata_generator.py` to generate csv food data. Function `food_data_generator('food_name.json',3)` reads
the json food list. number 3 represents that each row in `food_name.json` generates 3 rows in `foodlist_csvdata.csv`
3. Run `Foodlist_data_generator_with_db.py`. Make sure to configure the database name and password. Don't forget to 
comment them out when you commit the files to github. 


