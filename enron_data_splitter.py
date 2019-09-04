# Assumes you have the enron email dataset as emails.csv

import pandas as pd
data = pd.read_csv("../Datasets/emails.csv")
pd.set_option('display.max_colwidth',-1)
new = data["message"].str.split("\n", n = 15, expand = True) 

data["from"] = new[2]
data["fromn"] = new[8]
data["to"] = new[3]
data["ton"] = new[9]
data["subject"] = new[4]
data["msg"] = new[15]
data.drop(columns =["message"], inplace = True) 
data.drop(columns =["file"], inplace = True) 

data['from'] = data["from"].apply(lambda val: val.replace("From:",''))
data['fromn'] = data["fromn"].apply(lambda val: val.replace("X-From:",''))
data['to'] = data["to"].apply(lambda val: val.replace("To:",''))
data['ton'] = data["ton"].apply(lambda val: val.replace("X-To:",''))
data['subject'] = data["subject"].apply(lambda val: val.replace("Subject:",''))
data['msg'] = data["msg"].apply(lambda val: val.replace("\n",' '))

# Lets look only at emails with 100 words or less and that are Non-replies
data[(data['msg'].str.len() <100) & ~(data['subject'].str.contains('Re:'))].sample(5)