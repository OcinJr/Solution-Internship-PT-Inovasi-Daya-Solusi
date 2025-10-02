import pandas as pd
import os
import json


# No.1

# create a function to load all the JSON files inside a folder and normalize them then append the files into a data_list
def load_and_normalize(folder_path):
    data_list = []

    # loop into the folder, scanning all the files inside the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path,'r') as f:
            data = json.load(f)
            data_list.append(data)
            
    # normalize the datas inside data_list and update the data_list directly
    data_list = pd.json_normalize(data_list)
    
    # sort the datas inside data_list ny id and ts(timestamp)
    data_list.sort_values(by=['id','ts'])
    
    return data_list

# Feeling dataframe "df_accounts" with all the JSON data files located in "./data/accounts" using load_and_normalize function
df_accounts = load_and_normalize("./data/accounts")

# renaming and combining the features/columns
df_accounts["account_id"] = df_accounts["data.account_id"]
df_accounts["name"] = df_accounts["data.name"]
df_accounts["email"] = df_accounts["set.email"].combine_first(df_accounts["data.email"])
df_accounts["savings_account_id"] = df_accounts["set.savings_account_id"]
df_accounts["card_id"] = df_accounts["set.card_id"]

# combine only if there is a "set" column where it represents an update on the data with the same "name"
# combining column "set.address" with "data.address" into a new column named "address"
df_accounts["address"] = df_accounts["set.address"].combine_first(df_accounts["data.address"])

# combining column "set.phone_number" with "data.phone_number" into a new column named "phone_number"
df_accounts["phone_number"] = df_accounts["set.phone_number"].combine_first(df_accounts["data.phone_number"])

# choosing the needed columns that's been cleaned
cols = ["id","account_id","name","address","phone_number","email","savings_account_id","card_id"]
df_accounts = df_accounts[cols]

# grouping all the datas by using "id" as reference and feeling the empty data with the the ones above it (updating from the previous data
df_accounts = df_accounts.groupby("id").ffill()

print(f"\n{'='*41} - ACCOUNTS - {'='*41}")
print(df_accounts.to_string())

# Feeling dataframe "df_accounts" with all the JSON data files located in "./data/cards" using load_and_normalize function
df_cards = load_and_normalize("./data/cards")

# renaming and combining the features/columns
df_cards["card_id"] = df_cards["data.card_id"]
df_cards["card_number"] = df_cards["data.card_number"]
df_cards["monthly_limit"] = df_cards["data.monthly_limit"]

# combine only if there is a "set" column where it represents an update on the data with the same "name"
# combining column "set.credit_used" with "data.credit_used" into a new column named "credit_used"
df_cards["credit_used"] = df_cards["set.credit_used"].combine_first(df_cards["data.credit_used"])

# combining column "set.status" with "data.status" into a new column named "status"
df_cards["status"] = df_cards["set.status"].combine_first(df_cards["data.status"])

# choosing the needed columns that's been cleaned
cols = ["id","card_id","card_number","credit_used","monthly_limit","status"]
df_cards = df_cards[cols]

# grouping all the datas by using "id" as reference and feeling the empty data with the the ones above it (updating from the previous data
df_cards = df_cards.groupby("id").ffill()

print(f"\n{'='*23} - CARDS - {'='*24}")
print(df_cards.to_string())

# Feeling dataframe "df_accounts" with all the JSON data files located in "./data/cards" using load_and_normalize function
df_saving_accounts = load_and_normalize("./data/savings_accounts")

# renaming and combining the features/columns
df_saving_accounts["savings_account_id"] = df_saving_accounts["data.savings_account_id"]
df_saving_accounts["status"] = df_saving_accounts["data.status"]

# combine only if there is a "set" column where it represents an update on the data with the same "name"
# combining column "set.balance" with "data.balance" into a new column named "balance"
df_saving_accounts["balance"] = df_saving_accounts["set.balance"].combine_first(df_saving_accounts["data.balance"])

# combining column "set.interest_rate_percent" with "data.interest_rate_percent" into a new column named "interest_rate_percent"
df_saving_accounts["interest_rate_percent"] = df_saving_accounts["set.interest_rate_percent"].combine_first(df_saving_accounts["data.interest_rate_percent"])

# choosing the needed columns that's been cleaned
cols = ["id","savings_account_id","balance","interest_rate_percent","status"]
df_saving_accounts = df_saving_accounts[cols]

# grouping all the datas by using "id" as reference and feeling the empty data with the the ones above it (updating from the previous data)
df_saving_accounts = df_saving_accounts.groupby("id").ffill()

print(f"\n{'='*19} - SAVINGS ACCOUNTS - {'='*19}")
print(df_saving_accounts.to_string())
