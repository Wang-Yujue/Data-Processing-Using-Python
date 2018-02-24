import pandas
import numpy as np
data = pandas.read_table(r'/Users/wangyujue/Downloads/ml-100k/u.data', sep='\t', header=None)  # rate record
data.columns = ['user_id', 'item id', 'rating', 'timestamp']

user = pandas.read_table(r'/Users/wangyujue/Downloads/ml-100k/u.user', sep='|', header=None)  # user info
user.columns = ['user_id', 'age', 'gender', 'occupation', 'zip code']

Data = pandas.pivot_table(data, values='rating', columns=['user_id'], aggfunc='mean')
#User = user.pivot(index='gender', values='gender', columns='user_id')

#DATA = pandas.concat([Data,User])

F_user = user[user.gender == 'F']
M_user = user[user.gender == 'M']
print(F_user)
print(M_user)

DATA = Data.values[0]
F_rating = DATA[F_user.index]
M_rating = DATA[M_user.index]

F_std = np.std(F_rating)
M_std = np.std(M_rating)
print('Female:', F_std, 'Male:', M_std, sep='\n')

with open(r'std.txt', 'w') as f:
    f.write('4348')