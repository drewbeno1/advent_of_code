import pandas as pd


""" part 1 """

df = pd.read_table('input.txt', delim_whitespace=True, names=['a', 'b'])

df = df.apply(sorted)

difference = 0

difference += abs(df['a'] - df['b'])

# print(sum(difference))


""" part 2 """

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df1['id'] = df['a']
df2['id'] = df['b']

# join df2 into 1 with a left join and a resulting dataframe that is just the unique values in df1 and a count of how many times those values appear in df2
df = df1.merge(df2['id'].value_counts().reset_index(name="count"), on='id', how='left').fillna(0)

df['similarity'] = df['id'] * df['count']

print(sum(df['similarity']))

