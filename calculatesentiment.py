import pandas as pd
import numpy as np
from textblob import TextBlob

twedf = pd.read_csv("data/twitterdata.csv")
matchdf = pd.read_csv("data/matchdata.csv")

s = []
for i in range(matchdf['season'].size):
    testday = matchdf['date'][i][0:10]
    tweets = twedf[(twedf['Date']==testday)]['Tweet']
    li=[]
    for j in range(tweets.size):
        li.append(TextBlob(tweets.iloc[j]).sentiment[0])
    s.append(np.mean(li))

sdf = pd.DataFrame(s)
newdf = pd.concat([twedf,matchdf,sdf], axis=1)
newdf.to_csv(r'finaldata.csv',index=False)
