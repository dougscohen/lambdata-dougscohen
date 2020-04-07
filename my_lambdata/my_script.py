# this is where code will go

import pandas

from my_lambdata.my_mod import convert_to_seconds
from my_lambdata.my_mod import state_abbrev
from my_lambdata.another_mod import convert_names

print("This is a test")

print("--------------")
x = '2:14'
print(convert_to_seconds(x))

print("--------------")
y = 'Florida'
z = 'Marshall Islands'
print(state_abbrev(y))
print(state_abbrev(z))

print("--------------")
df3 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
full_df3 = convert_names(df3)
print(full_df3.head())