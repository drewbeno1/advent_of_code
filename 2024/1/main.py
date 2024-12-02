import pandas as pd

df = pd.read_table('input.txt', delim_whitespace=True, names=['a', 'b'])

df = df.apply(sorted)

difference = 0

difference += abs(df['a'] - df['b'])

print(sum(difference))

