import re
import pandas as pd
import _0_configurations as conf

data = pd.read_csv('input/'+str(conf.NEWS_ACOUNT)+'.csv')

pat = '|'.join(map(re.escape, conf.keywords[conf.ASSET]))
data['is_true'] = data.headline_text.str.contains(pat)

print(data[data['is_true']==True].shape)
data = data[data['is_true']==True]

data = data.drop(['is_true'], axis=1)

data.to_csv('input/'+str(conf.NEWS_ACOUNT)+'_'+str(conf.ASSET)+'.csv', index=False)