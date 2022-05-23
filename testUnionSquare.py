import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
import pandas as pd

UnionSquare = pd.read_csv('/home/dba/realestate/UnionSquareMA-trimmed-C.csv')

UnionSquare.head()

UnionSquare.SoldPrice = UnionSquare.SoldPrice.str.replace('$', '')
UnionSquare.SoldPrice = UnionSquare.SoldPrice.str.replace(',', '')

note = pd.to_numeric(UnionSquare.SoldPrice)

note2 = UnionSquare.head()

#print(note)
#print(note2)

UnionSquare['SoldPrice'] = UnionSquare['SoldPrice'].astype(float)
a=UnionSquare['SoldPrice'].sum()
b=UnionSquare['InteriorSqFt'].sum()

AvgCostPerSqFt = str(round(a/b, 2))

print('AverageCostPerSqFt is $',AvgCostPerSqFt)
