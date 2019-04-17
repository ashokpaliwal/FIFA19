Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> import os
>>> print(os.listdir("/users/ashokpaliwal/DESKTOP/DATA-SCIENCE/Projects/fifa19"))
['.DS_Store', 'fifa19.csv']
>>> data = pd.read_csv ('/users/ashokpaliwal/DESKTOP/DATA-SCIENCE/Projects/fifa19/fifa19.csv')
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18207 entries, 0 to 18206
Data columns (total 89 columns):
Unnamed: 0                  18207 non-null int64
ID                          18207 non-null int64
Name                        18207 non-null object
Age                         18207 non-null int64
Photo                       18207 non-null object
Nationality                 18207 non-null object
Flag                        18207 non-null object
Overall                     18207 non-null int64
Potential                   18207 non-null int64
Club                        17966 non-null object
Club Logo                   18207 non-null object
Value                       18207 non-null object
Wage                        18207 non-null object
Special                     18207 non-null int64
Preferred Foot              18159 non-null object
International Reputation    18159 non-null float64
Weak Foot                   18159 non-null float64
Skill Moves                 18159 non-null float64
Work Rate                   18159 non-null object
Body Type                   18159 non-null object
Real Face                   18159 non-null object
Position                    18147 non-null object
Jersey Number               18147 non-null float64
Joined                      16654 non-null object
Loaned From                 1264 non-null object
Contract Valid Until        17918 non-null object
Height                      18159 non-null object
Weight                      18159 non-null object
LS                          16122 non-null object
ST                          16122 non-null object
RS                          16122 non-null object
LW                          16122 non-null object
LF                          16122 non-null object
CF                          16122 non-null object
RF                          16122 non-null object
RW                          16122 non-null object
LAM                         16122 non-null object
CAM                         16122 non-null object
RAM                         16122 non-null object
LM                          16122 non-null object
LCM                         16122 non-null object
CM                          16122 non-null object
RCM                         16122 non-null object
RM                          16122 non-null object
LWB                         16122 non-null object
LDM                         16122 non-null object
CDM                         16122 non-null object
RDM                         16122 non-null object
RWB                         16122 non-null object
LB                          16122 non-null object
LCB                         16122 non-null object
CB                          16122 non-null object
RCB                         16122 non-null object
RB                          16122 non-null object
Crossing                    18159 non-null float64
Finishing                   18159 non-null float64
HeadingAccuracy             18159 non-null float64
ShortPassing                18159 non-null float64
Volleys                     18159 non-null float64
Dribbling                   18159 non-null float64
Curve                       18159 non-null float64
FKAccuracy                  18159 non-null float64
LongPassing                 18159 non-null float64
BallControl                 18159 non-null float64
Acceleration                18159 non-null float64
SprintSpeed                 18159 non-null float64
Agility                     18159 non-null float64
Reactions                   18159 non-null float64
Balance                     18159 non-null float64
ShotPower                   18159 non-null float64
Jumping                     18159 non-null float64
Stamina                     18159 non-null float64
Strength                    18159 non-null float64
LongShots                   18159 non-null float64
Aggression                  18159 non-null float64
Interceptions               18159 non-null float64
Positioning                 18159 non-null float64
Vision                      18159 non-null float64
Penalties                   18159 non-null float64
Composure                   18159 non-null float64
Marking                     18159 non-null float64
StandingTackle              18159 non-null float64
SlidingTackle               18159 non-null float64
GKDiving                    18159 non-null float64
GKHandling                  18159 non-null float64
GKKicking                   18159 non-null float64
GKPositioning               18159 non-null float64
GKReflexes                  18159 non-null float64
Release Clause              16643 non-null object
dtypes: float64(38), int64(6), object(45)
memory usage: 12.4+ MB

>>> data.describe()
         Unnamed: 0             ID  ...  GKPositioning    GKReflexes
count  18207.000000   18207.000000  ...   18159.000000  18159.000000
mean    9103.000000  214298.338606  ...      16.388898     16.710887
std     5256.052511   29965.244204  ...      17.034669     17.955119
min        0.000000      16.000000  ...       1.000000      1.000000
25%     4551.500000  200315.500000  ...       8.000000      8.000000
50%     9103.000000  221759.000000  ...      11.000000     11.000000
75%    13654.500000  236529.500000  ...      14.000000     14.000000
max    18206.000000  246620.000000  ...      90.000000     94.000000

[8 rows x 44 columns]
>>> data.head()
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M

[5 rows x 89 columns]
>>> data.tail()
       Unnamed: 0      ID  ... GKReflexes  Release Clause
18202       18202  238813  ...        9.0           €143K
18203       18203  243165  ...       12.0           €113K
18204       18204  241638  ...       13.0           €165K
18205       18205  246268  ...        9.0           €143K
18206       18206  246269  ...        9.0           €165K

[5 rows x 89 columns]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> data.Finishing.plot(kind = 'line', color = 'g', label = 'Finishing', linewidth = 1, alpha = 0.5, grid = True, linestyle = ':')
<matplotlib.axes._subplots.AxesSubplot object at 0x1192887b8>
>>> data.Positioning.plot(color = 'r', label = 'Positioning', linewidth = 1, alpha = 0.5, grid = True, linestyle = '-.')
<matplotlib.axes._subplots.AxesSubplot object at 0x1192887b8>
>>> plt.legend(loc='upper right')
<matplotlib.legend.Legend object at 0x10e80b278>
>>> plt.xlabel('x axis')
Text(0.5, 0, 'x axis')
>>> plt.ylabel('y axis')
Text(0, 0.5, 'y axis')
>>> plt.title('Line Plot')
Text(0.5, 1.0, 'Line Plot')
>>> plt.show()
>>> 
>>> 
>>> 
>>> data.plot(kind='scatter', x = 'Special', y = 'Skill Moves', alpha = 0.5, color = 'red')
<matplotlib.axes._subplots.AxesSubplot object at 0x11a0e9c50>
>>> plt.xlabel('Special)
	       
SyntaxError: EOL while scanning string literal
>>> plt.xlabel('Special')
	       
Text(0.5, 0, 'Special')
>>> plt.ylabel('Special Skill Moves Scatter PLot')
	       
Text(0, 0.5, 'Special Skill Moves Scatter PLot')
>>> plt.show()
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> data.SprintSpeed.plot(kind= 'hist', bins = 50, figsize= (12,12))
	       
<matplotlib.axes._subplots.AxesSubplot object at 0x119ca14a8>
>>> plt.show()
	       
>>> 
	       
>>> 
	       
>>> data.SprintSpeed.plot(kind = 'hist', bins = 50)
	       
<matplotlib.axes._subplots.AxesSubplot object at 0x11b340a90>
>>> plt.clf()
	       
>>> 
	       
>>> dictionary : {'istanbul': 'besiktas', 'paris' : 'psg'}
	       
>>> dict_keys(['istanbul', 'paris'])
	       
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict_keys(['istanbul', 'paris'])
NameError: name 'dict_keys' is not defined
>>> print("dictionary:", diciotnary)
	       
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print("dictionary:", diciotnary)
NameError: name 'diciotnary' is not defined
>>> print("dictionary:", dictionary)
	       
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("dictionary:", dictionary)
NameError: name 'dictionary' is not defined
>>> dictionary = {'istanbul': 'besiktas' , 'paris' : 'psg'}
	       
>>> print("dictionary:", dictionary)
	       
dictionary: {'istanbul': 'besiktas', 'paris': 'psg'}
>>> print(dictionar.keys())
	       
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(dictionar.keys())
NameError: name 'dictionar' is not defined
>>> print(dictionary.keys())
	       
dict_keys(['istanbul', 'paris'])
>>> print(dictionary.values())
	       
dict_values(['besiktas', 'psg'])
>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       

>>> dictionary ['istanbul'] = "galatasaray"
	       
>>> print(dictionary)
	       
{'istanbul': 'galatasaray', 'paris': 'psg'}
>>> dictionary['madrid'] = "realmadrid"
	       
>>> print(dictionary)
	       
{'istanbul': 'galatasaray', 'paris': 'psg', 'madrid': 'realmadrid'}
>>> 
	       
>>> 
	       
>>> del dictionary ['istanbul']
	       
>>> print(dictionary)
	       
{'paris': 'psg', 'madrid': 'realmadrid'}
>>> print ('paris' in dictionary)
	       
True
>>> dictionary.clear()
	       
>>> print(dictionary)
	       
{}
>>> print(dictionary)
	       
{}
>>> 
	       
>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       

>>> 
	       
>>> series = data['club']
	       
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2656, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'club'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    series = data['club']
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2658, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'club'
>>> series = data['Club']
	       
>>> print(type(series))
	       
<class 'pandas.core.series.Series'>
>>> data_frame = data[['Agility']]
	       
>>> print(type(data_frame))
	       
<class 'pandas.core.frame.DataFrame'>
>>> 
	       
>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       

>>> x = data['Age'] > 43
	       
>>> data[x]
	       
       Unnamed: 0      ID  ... GKReflexes  Release Clause
4741         4741  140029  ...       74.0           €272K
17726       17726   51963  ...       44.0             NaN
18183       18183   53748  ...       46.0             NaN

[3 rows x 89 columns]
>>> [3 rows x 89 columns]
	       
SyntaxError: invalid syntax
>>> 
	       
>>> 
	       
>>> data[np.logical_and(data['Age'] > 43, data['Potential'] < 60]
	 
SyntaxError: invalid syntax
>>> data.[np.logical_and(data['Age']>43,data['Potential']<60)]
	 
SyntaxError: invalid syntax
>>> data[np.logical_and(data['Age']>43, data['Potential']<60)]
	 
       Unnamed: 0     ID  ... GKReflexes  Release Clause
17726       17726  51963  ...       44.0             NaN
18183       18183  53748  ...       46.0             NaN

[2 rows x 89 columns]
>>> 
	 
>>> 
	 
>>> data.collumns
	 
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    data.collumns
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'collumns'
>>> data.columns
	 
Index(['Unnamed: 0', 'ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag',
       'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Special',
       'Preferred Foot', 'International Reputation', 'Weak Foot',
       'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position',
       'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until',
       'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause'],
      dtype='object')
>>> 
	 
>>> 
	 
>>> 
	 
>>> 
	 
>>> data[(data['Age']>40) & (data['Potential']<60)]
	 
       Unnamed: 0     ID  ... GKReflexes  Release Clause
15426       15426  18745  ...       55.0            €18K
17726       17726  51963  ...       44.0             NaN
18183       18183  53748  ...       46.0             NaN

[3 rows x 89 columns]
>>> 
	 
>>> dictionary = {'spain':'barcelona','france':'psg'}
	 
>>> for key,value in data [['Value']][0:6].iterrows():
	 print(index, ":",value)

	 
Traceback (most recent call last):
  File "<pyshell#109>", line 2, in <module>
    print(index, ":",value)
NameError: name 'index' is not defined
>>> 
	 
>>> 
	 
>>> 
	 
>>> dictionary = {'spain':'barcelona','france':'psg'}
	 
>>> for key,value in dictionary.items():
	 print(key,":",value)

	 
spain : barcelona
france : psg
>>> print('')
	 

>>> for index,value in data[['Value']][0:6].iterrows():
	 print (index,":",value)

	 
0 : Value    €110.5M
Name: 0, dtype: object
1 : Value    €77M
Name: 1, dtype: object
2 : Value    €118.5M
Name: 2, dtype: object
3 : Value    €72M
Name: 3, dtype: object
4 : Value    €102M
Name: 4, dtype: object
5 : Value    €93M
Name: 5, dtype: object
>>> 
	 
>>> 
	 
>>> def fake_func():
	 """return defined t tuble"""
	 t = (1,2,3)
	 return t

>>> a,b,c = fake_func()
	 
>>> print(a,b,c)
	 
1 2 3
>>> 
	 
>>> 
	 
>>> 
	 
>>> 
	 
>>> 
	 
>>> import builtins
	 
>>> dir(builtins)
	 
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
	 
>>> 
	 
>>> 
	 
>>> threshold = sum(data.Potential)/len(data.Potential)
	 
>>> print(threshold)
	 
71.30729939034437
>>> data["pot_level"] = ["high" if i > threshold else "low" for i in data.Potential]
	 
>>> data.loc[:10,["pot_level", "Potential"]]
	 
   pot_level  Potential
0       high         94
1       high         94
2       high         93
3       high         93
4       high         92
5       high         91
6       high         91
7       high         91
8       high         91
9       high         93
10      high         90
>>> 
	 
>>> 
	 
>>> 
	 
>>> 
	 

>>> 
	 

>>> data = pd.read_csv('/users/ashokpaliwal/DESKTOP/DATA-SCIENCE/Projects/fifa19/fifa19.csv')
	 
>>> data.head(10)
	 
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M
5           5  183277  ...        8.0         €172.1M
6           6  177003  ...        9.0         €137.4M
7           7  176580  ...       37.0           €164M
8           8  155862  ...       11.0         €104.6M
9           9  200389  ...       89.0         €144.5M

[10 rows x 89 columns]
>>> 
	 
>>> 
	 
>>> data.head(10)
	 
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M
5           5  183277  ...        8.0         €172.1M
6           6  177003  ...        9.0         €137.4M
7           7  176580  ...       37.0           €164M
8           8  155862  ...       11.0         €104.6M
9           9  200389  ...       89.0         €144.5M

[10 rows x 89 columns]
>>> 
	 
>>> data.info()
	 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18207 entries, 0 to 18206
Data columns (total 89 columns):
Unnamed: 0                  18207 non-null int64
ID                          18207 non-null int64
Name                        18207 non-null object
Age                         18207 non-null int64
Photo                       18207 non-null object
Nationality                 18207 non-null object
Flag                        18207 non-null object
Overall                     18207 non-null int64
Potential                   18207 non-null int64
Club                        17966 non-null object
Club Logo                   18207 non-null object
Value                       18207 non-null object
Wage                        18207 non-null object
Special                     18207 non-null int64
Preferred Foot              18159 non-null object
International Reputation    18159 non-null float64
Weak Foot                   18159 non-null float64
Skill Moves                 18159 non-null float64
Work Rate                   18159 non-null object
Body Type                   18159 non-null object
Real Face                   18159 non-null object
Position                    18147 non-null object
Jersey Number               18147 non-null float64
Joined                      16654 non-null object
Loaned From                 1264 non-null object
Contract Valid Until        17918 non-null object
Height                      18159 non-null object
Weight                      18159 non-null object
LS                          16122 non-null object
ST                          16122 non-null object
RS                          16122 non-null object
LW                          16122 non-null object
LF                          16122 non-null object
CF                          16122 non-null object
RF                          16122 non-null object
RW                          16122 non-null object
LAM                         16122 non-null object
CAM                         16122 non-null object
RAM                         16122 non-null object
LM                          16122 non-null object
LCM                         16122 non-null object
CM                          16122 non-null object
RCM                         16122 non-null object
RM                          16122 non-null object
LWB                         16122 non-null object
LDM                         16122 non-null object
CDM                         16122 non-null object
RDM                         16122 non-null object
RWB                         16122 non-null object
LB                          16122 non-null object
LCB                         16122 non-null object
CB                          16122 non-null object
RCB                         16122 non-null object
RB                          16122 non-null object
Crossing                    18159 non-null float64
Finishing                   18159 non-null float64
HeadingAccuracy             18159 non-null float64
ShortPassing                18159 non-null float64
Volleys                     18159 non-null float64
Dribbling                   18159 non-null float64
Curve                       18159 non-null float64
FKAccuracy                  18159 non-null float64
LongPassing                 18159 non-null float64
BallControl                 18159 non-null float64
Acceleration                18159 non-null float64
SprintSpeed                 18159 non-null float64
Agility                     18159 non-null float64
Reactions                   18159 non-null float64
Balance                     18159 non-null float64
ShotPower                   18159 non-null float64
Jumping                     18159 non-null float64
Stamina                     18159 non-null float64
Strength                    18159 non-null float64
LongShots                   18159 non-null float64
Aggression                  18159 non-null float64
Interceptions               18159 non-null float64
Positioning                 18159 non-null float64
Vision                      18159 non-null float64
Penalties                   18159 non-null float64
Composure                   18159 non-null float64
Marking                     18159 non-null float64
StandingTackle              18159 non-null float64
SlidingTackle               18159 non-null float64
GKDiving                    18159 non-null float64
GKHandling                  18159 non-null float64
GKKicking                   18159 non-null float64
GKPositioning               18159 non-null float64
GKReflexes                  18159 non-null float64
Release Clause              16643 non-null object
dtypes: float64(38), int64(6), object(45)
memory usage: 12.4+ MB

>>> StandingTackle              18159 non-null float64
	 
SyntaxError: invalid syntax
>>> 
	 
>>> 
	 
>>> print(data['Nationality'].value_counts(dropna = False))
	 
England                 1662
Germany                 1198
Spain                   1072
Argentina                937
France                   914
Brazil                   827
Italy                    702
Colombia                 618
Japan                    478
Netherlands              453
Sweden                   397
China PR                 392
Chile                    391
Republic of Ireland      368
Mexico                   366
United States            353
Poland                   350
Norway                   341
Saudi Arabia             340
Denmark                  336
Korea Republic           335
Portugal                 322
Turkey                   303
Austria                  298
Scotland                 286
Belgium                  260
Australia                236
Switzerland              220
Uruguay                  149
Senegal                  130
                        ... 
Nicaragua                  2
Dominican Republic         2
Bermuda                    2
Eritrea                    2
Chad                       2
Uzbekistan                 2
United Arab Emirates       1
South Sudan                1
Belize                     1
Rwanda                     1
Liberia                    1
Andorra                    1
Jordan                     1
Qatar                      1
Fiji                       1
São Tomé & Príncipe        1
Ethiopia                   1
Indonesia                  1
Oman                       1
Malta                      1
St Lucia                   1
Botswana                   1
Kuwait                     1
Grenada                    1
Mauritius                  1
Palestine                  1
Puerto Rico                1
Guam                       1
New Caledonia              1
Lebanon                    1
Name: Nationality, Length: 164, dtype: int64
>>> 
	 
>>> data.describe()
	 
         Unnamed: 0             ID  ...  GKPositioning    GKReflexes
count  18207.000000   18207.000000  ...   18159.000000  18159.000000
mean    9103.000000  214298.338606  ...      16.388898     16.710887
std     5256.052511   29965.244204  ...      17.034669     17.955119
min        0.000000      16.000000  ...       1.000000      1.000000
25%     4551.500000  200315.500000  ...       8.000000      8.000000
50%     9103.000000  221759.000000  ...      11.000000     11.000000
75%    13654.500000  236529.500000  ...      14.000000     14.000000
max    18206.000000  246620.000000  ...      90.000000     94.000000

[8 rows x 44 columns]
>>> 
	 
>>> data.boxplot(column = 'Potential', by = 'Real Face')
	 
<matplotlib.axes._subplots.AxesSubplot object at 0x110395668>
>>> plt.show()
	 
>>> 
	 
>>> data_new = data.head()
	 
>>> data_new
	 
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M

[5 rows x 89 columns]
>>> 
	 
>>> melted = pd.melt(frame = data_new, id_vars = 'Name', value_vars = ['Nationality', 'Club'])
	 
>>> melted
	 
                Name     variable                value
0           L. Messi  Nationality            Argentina
1  Cristiano Ronaldo  Nationality             Portugal
2          Neymar Jr  Nationality               Brazil
3             De Gea  Nationality                Spain
4       K. De Bruyne  Nationality              Belgium
5           L. Messi         Club         FC Barcelona
6  Cristiano Ronaldo         Club             Juventus
7          Neymar Jr         Club  Paris Saint-Germain
8             De Gea         Club    Manchester United
9       K. De Bruyne         Club      Manchester City
>>> 
	 
>>> 
	 
>>> melted.pivot(index = 'Name', columns = 'variable', values = 'value')
	 
variable                          Club Nationality
Name                                              
Cristiano Ronaldo             Juventus    Portugal
De Gea               Manchester United       Spain
K. De Bruyne           Manchester City     Belgium
L. Messi                  FC Barcelona   Argentina
Neymar Jr          Paris Saint-Germain      Brazil
>>> 
	 
>>> 
	 
>>> data1 = data.head()
	 
>>> data2 = data.tail()
	 
>>> conc_data_row = pd.concat([data1, data2], axis = 0, ignore_index = True)
	 
>>> conc_data_row
	 
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M
5       18202  238813  ...        9.0           €143K
6       18203  243165  ...       12.0           €113K
7       18204  241638  ...       13.0           €165K
8       18205  246268  ...        9.0           €143K
9       18206  246269  ...        9.0           €165K

[10 rows x 89 columns]
>>> 
	 
>>> data1 = data['Nationality'].head()
	 
>>> data2 = data['Value'].head()
	 
>>> data3 = data['Name'].head()
	 
>>> conc_data_col = pd.concat([data3, data2, data1],axis= 1)
	 
>>> conc_data_col
	 
                Name    Value Nationality
0           L. Messi  €110.5M   Argentina
1  Cristiano Ronaldo     €77M    Portugal
2          Neymar Jr  €118.5M      Brazil
3             De Gea     €72M       Spain
4       K. De Bruyne    €102M     Belgium
>>> 
	 
>>> 
	 
>>> data.dtypes.head(10)
	 
Unnamed: 0      int64
ID              int64
Name           object
Age             int64
Photo          object
Nationality    object
Flag           object
Overall         int64
Potential       int64
Club           object
dtype: object
>>> ID              int64
	 
SyntaxError: invalid syntax
>>> 
	 
>>> 
	 
>>> 
	 
>>> data['Nationality'] = data['Nationality'].astype ('category')
	 
>>> data['Age'] = data['Age'].astype('float')
	 
>>> data.dtypes.head(10)
	 
Unnamed: 0        int64
ID                int64
Name             object
Age             float64
Photo            object
Nationality    category
Flag             object
Overall           int64
Potential         int64
Club             object
dtype: object
>>> 
	 
>>> 
	 
>>> data["Club"].value_counts(dropna = False)
	 
NaN                          241
Real Madrid                   33
Eintracht Frankfurt           33
RC Celta                      33
Empoli                        33
Burnley                       33
Southampton                   33
Manchester United             33
Manchester City               33
Tottenham Hotspur             33
Fortuna Düsseldorf            33
Borussia Dortmund             33
Cardiff City                  33
Valencia CF                   33
Atlético Madrid               33
FC Barcelona                  33
Liverpool                     33
TSG 1899 Hoffenheim           33
Arsenal                       33
Wolverhampton Wanderers       33
Chelsea                       33
AS Monaco                     33
Newcastle United              33
CD Leganés                    33
Everton                       33
Frosinone                     33
Rayo Vallecano                33
Leicester City                32
FC Nantes                     32
SV Werder Bremen              32
                            ... 
Chicago Fire                  23
GFC Ajaccio                   23
Kasimpaşa SK                  23
St. Patrick's Athletic        23
Clube Sport Marítimo          23
Shamrock Rovers               22
FK Haugesund                  22
Östersunds FK                 22
Wellington Phoenix            21
Dalkurd FF                    21
Melbourne Victory             21
Vitória                       20
Botafogo                      20
Chapecoense                   20
Atlético Paranaense           20
Atlético Mineiro              20
Sport Club do Recife          20
Tromsø IL                     20
Bahia                         20
Cruzeiro                      20
Ceará Sporting Club           20
Paraná                        20
Grêmio                        20
Internacional                 20
América FC (Minas Gerais)     20
Fluminense                    20
Santos                        20
Sligo Rovers                  19
Limerick FC                   19
Derry City                    18
Name: Club, Length: 652, dtype: int64
>>> 
	 
>>> 
	 
>>> data1 = data
	 
>>> data1["Club"].dropna(inplace = True)
	 
>>> assert == 1
	 
SyntaxError: invalid syntax
>>> assert 1==1
	 
>>> assert data['Club'].notnull().all()
	 
>>> data["Club"].fillna('empty',inplace = True)
	 
>>> assert data['Club'].notnull().all()
	 
>>> data = data.drop(['ID', 'Photo', 'Flag'], axis = 1)
	 
>>> data.head()
	 
   Unnamed: 0               Name  ...  GKReflexes Release Clause
0           0           L. Messi  ...         8.0        €226.5M
1           1  Cristiano Ronaldo  ...        11.0        €127.1M
2           2          Neymar Jr  ...        11.0        €228.1M
3           3             De Gea  ...        94.0        €138.6M
4           4       K. De Bruyne  ...        13.0        €196.4M

[5 rows x 86 columns]
>>> 
	 
>>> threshold1 = data.Dribbling.mean()
	 
>>> print(threshold1)
	 
55.37100060576023
>>> data["fin_level"] = ["high" if i > threshold1 else "low" for i in data.Finishing]
	 
>>> data.loc[:10,["fin_level","Finishing"]]
	 
   fin_level  Finishing
0       high       95.0
1       high       94.0
2       high       87.0
3        low       13.0
4       high       82.0
5       high       84.0
6       high       72.0
7       high       93.0
8       high       60.0
9        low       11.0
10      high       91.0
>>> 
	 
>>> turk = data.Nationality == 'Turkey'
	 
>>> data[turk]
	 
       Unnamed: 0           Name   Age  ... GKReflexes  Release Clause  fin_level
383           383      O. Toprak  28.0  ...       15.0          €28.4M        low
449           449  H. Çalhanoğlu  24.0  ...       10.0          €34.6M       high
659           659       C. Tosun  27.0  ...        9.0          €28.6M       high
705           705       N. Şahin  29.0  ...       11.0            €17M       high
721           721      B. Yılmaz  32.0  ...       12.0            €20M       high
725           725   E. Belözoğlu  37.0  ...        8.0           €7.6M       high
853           853     O. Özyakup  25.0  ...       13.0          €25.7M       high
908           908       E. Çolak  27.0  ...        7.0          €16.2M       high
930           930      E. Akbaba  25.0  ...        8.0          €21.7M       high
977           977      O. Kıvrak  30.0  ...       81.0            €11M        low
1024         1024     V. Babacan  29.0  ...       78.0          €13.8M        low
1029         1029       C. Ünder  20.0  ...        8.0          €27.6M       high
1045         1045       A. Turan  31.0  ...       11.0             NaN       high
1064         1064     O. Yokuşlu  24.0  ...        7.0          €24.2M       high
1139         1139        S. Aziz  27.0  ...       10.0          €16.8M        low
1161         1161        E. Ünal  21.0  ...       13.0             NaN       high
1291         1291        G. Töre  26.0  ...       11.0          €17.8M       high
1332         1332       G. Gönül  33.0  ...       10.0           €5.6M       high
1358         1358       C. Erkin  29.0  ...       13.0          €11.4M       high
1501         1501      Y. Yazıcı  21.0  ...        7.0          €24.2M       high
1525         1525       M. Topal  32.0  ...       11.0           €8.4M       high
1557         1557       H. Tekin  29.0  ...       80.0          €11.9M        low
1634         1634       A. Potuk  27.0  ...        8.0          €14.8M       high
1652         1652     O. Şahiner  26.0  ...        9.0          €16.6M       high
1925         1925       K. Ayhan  23.0  ...       10.0          €14.1M        low
1929         1929     M. Çağıran  25.0  ...        7.0          €14.5M       high
1947         1947     C. Söyüncü  22.0  ...        7.0          €17.9M        low
1959         1959        S. İnan  33.0  ...       16.0           €7.4M       high
2033         2033       D. Türüç  25.0  ...       13.0          €17.6M       high
2095         2095     V. Demirel  36.0  ...       73.0           €1.4M        low
...           ...            ...   ...  ...        ...             ...        ...
16448       16448     O. Özdemir  20.0  ...        9.0           €273K        low
16525       16525       F. Zorba  20.0  ...       13.0           €231K        low
16569       16569    A. Bayındır  20.0  ...       57.0           €264K        low
16616       16616     V. Karakuş  20.0  ...       64.0           €286K        low
16640       16640      U. Türker  20.0  ...       14.0           €604K        low
16657       16657        F. Kaya  18.0  ...       11.0           €490K       high
16702       16702       O. Malcı  22.0  ...       10.0           €264K        low
16729       16729     G. Kımışır  20.0  ...       13.0           €264K        low
16738       16738     A. Koldere  18.0  ...        7.0           €429K        low
16810       16810        S. Tağa  26.0  ...        6.0           €228K        low
16812       16812       O. Şahin  20.0  ...       12.0           €280K        low
16852       16852      S. Farsak  20.0  ...        6.0           €252K        low
16855       16855     Y. Avcılar  19.0  ...        8.0           €455K        low
16868       16868      Y. Mersin  23.0  ...       59.0           €195K        low
16909       16909        I. Ünal  20.0  ...       58.0           €368K        low
17004       17004   B. Delihasan  19.0  ...       13.0           €473K        low
17074       17074        H. Acar  23.0  ...       12.0           €264K        low
17091       17091       A. Doğan  16.0  ...        8.0           €420K        low
17125       17125   E. Çetindere  18.0  ...        5.0           €540K        low
17127       17127      F. Durmuş  19.0  ...        5.0           €499K        low
17139       17139       E. Selen  23.0  ...       52.0           €198K        low
17182       17182       S. Bakan  17.0  ...       14.0           €473K        low
17378       17378   S. Gucciardo  19.0  ...        8.0           €210K        low
17387       17387       A. Damlu  18.0  ...       55.0           €289K        low
17452       17452       A. Aktas  18.0  ...        8.0           €420K        low
17581       17581    S. Sarıkaya  18.0  ...        8.0           €315K        low
17759       17759      M. Yıldız  19.0  ...       54.0           €132K        low
18046       18046     K. Civelek  20.0  ...       47.0            €65K        low
18050       18050  E. Destanoglu  17.0  ...       52.0           €145K        low
18093       18093       E. Bilen  17.0  ...       50.0           €131K        low

[303 rows x 87 columns]
>>> 
	 
>>> 
	 
>>> country = ["Spain", "France"]
	 
>>> team = ["realmadrid", "psg"]
	 
>>> list_label = ["country", "team"]
	 
>>> list_col = [country, team]
	 
>>> zipped = list(zip(list_label, list_col))
	 
>>> data_dict = dict(zipped)
	 
>>> df = pd.DataFrame(data_dict)
	 
>>> df
	 
  country        team
0   Spain  realmadrid
1  France         psg
>>> 
	 

>>> 
	 
>>> df["capital"] = ["madrid","paris"]
	 
>>> df
	 
  country        team capital
0   Spain  realmadrid  madrid
1  France         psg   paris
>>> df["valaue"] = 0
	 
>>> df
	 
  country        team capital  valaue
0   Spain  realmadrid  madrid       0
1  France         psg   paris       0
>>> 
	 
>>> data1 = data.loc[:,["Age", "Potential","Overall"]]
	 
>>> data1.plot()
	 
<matplotlib.axes._subplots.AxesSubplot object at 0x1112ab828>
>>> plt.show()
	 
>>> 
	 
>>> data1.plot(subplots = True)
	 
array([<matplotlib.axes._subplots.AxesSubplot object at 0x1112ab198>,
       <matplotlib.axes._subplots.AxesSubplot object at 0x11a04cac8>,
       <matplotlib.axes._subplots.AxesSubplot object at 0x11a071be0>],
      dtype=object)
>>> plt.show()
	 
>>> 
	 
>>> data1.plot(kind = "scatter", x = "Potential", y = "Overall")
	 
<matplotlib.axes._subplots.AxesSubplot object at 0x11b6539e8>
>>> plt.show()
	 
>>> 
	 
>>> data1.plot(kind="hist",y= "Age", bins = 50, range= (0,50), normed = True )
	 

Warning (from warnings module):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/axes/_axes.py", line 6521
    alternative="'density'", removal="3.1")
MatplotlibDeprecationWarning: 
The 'normed' kwarg was deprecated in Matplotlib 2.1 and will be removed in 3.1. Use 'density' instead.
<matplotlib.axes._subplots.AxesSubplot object at 0x11bf77dd8>
>>> plt.show()
	       

>>> 
	       
>>> fig,axes = plt.subplots(nrows=2, ncols = 1)
	       
>>> data1.plot(kind = "hist", y = "Age", bins = 50, range = (0,50), density = True, ax = axes[0])
	       
<matplotlib.axes._subplots.AxesSubplot object at 0x11c09bb70>
>>> data1.plt(kind= "hist", y = "Age", bins =50, range = (0,50), density = True, ax = axes[1], cumulative = True)
	       
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    data1.plt(kind= "hist", y = "Age", bins =50, range = (0,50), density = True, ax = axes[1], cumulative = True)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'plt'
>>> data1.plot(kind= "hist", y = "Age", bins =50, range = (0,50), density = True, ax = axes[1], cumulative = True)
	       
<matplotlib.axes._subplots.AxesSubplot object at 0x11c0d2a58>
>>> plt.savefig('graph.png')
	       
>>> plt
	       
<module 'matplotlib.pyplot' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/pyplot.py'>
>>> plt.show()
	       
>>> 
	       
>>> data.describe()
	       
         Unnamed: 0           Age  ...  GKPositioning    GKReflexes
count  18207.000000  18207.000000  ...   18159.000000  18159.000000
mean    9103.000000     25.122206  ...      16.388898     16.710887
std     5256.052511      4.669943  ...      17.034669     17.955119
min        0.000000     16.000000  ...       1.000000      1.000000
25%     4551.500000     21.000000  ...       8.000000      8.000000
50%     9103.000000     25.000000  ...      11.000000     11.000000
75%    13654.500000     28.000000  ...      14.000000     14.000000
max    18206.000000     45.000000  ...      90.000000     94.000000

[8 rows x 43 columns]
>>> 
	       
>>> data = pd.read_csv(/user/ashokpaliwal/DESKTOP/DATA-SCIENCE/fifa19/fifa19.csv)
	       
SyntaxError: invalid syntax
>>> data = pd.read_csv(user/ashokpaliwal/DESKTOP/DATA-SCIENCE/fifa19/fifa19.csv)
	       
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    data = pd.read_csv(user/ashokpaliwal/DESKTOP/DATA-SCIENCE/fifa19/fifa19.csv)
NameError: name 'user' is not defined
>>> data = pd.read_csv('/users/ashokpaliwal/DESKTOP/DATA-SCIENCE/Projects/fifa19/fifa19.csv')
	       
>>> data = data.set_index("Unnamed : 0")
	       
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2656, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Unnamed : 0'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    data = data.set_index("Unnamed : 0")
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 4178, in set_index
    level = frame[col]._values
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2658, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Unnamed : 0'
>>> data = data.set_index("Unnamed: 0")
	       
>>> data.head()
	       
                ID               Name  ...  GKReflexes Release Clause
Unnamed: 0                             ...                           
0           158023           L. Messi  ...         8.0        €226.5M
1            20801  Cristiano Ronaldo  ...        11.0        €127.1M
2           190871          Neymar Jr  ...        11.0        €228.1M
3           193080             De Gea  ...        94.0        €138.6M
4           192985       K. De Bruyne  ...        13.0        €196.4M

[5 rows x 88 columns]
>>> 
	       
>>> data["Nationality"][1]
	       
'Portugal'
>>> data.nationality[1]
	       
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    data.nationality[1]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'nationality'
>>> data.Nationality[1]
	       
'Portugal'
>>> data.loc[1,["Nationality"]]
	       
Nationality    Portugal
Name: 1, dtype: object
>>> data[["Name", "Nationality"]]
	       
                            Name          Nationality
Unnamed: 0                                           
0                       L. Messi            Argentina
1              Cristiano Ronaldo             Portugal
2                      Neymar Jr               Brazil
3                         De Gea                Spain
4                   K. De Bruyne              Belgium
5                      E. Hazard              Belgium
6                      L. Modrić              Croatia
7                      L. Suárez              Uruguay
8                   Sergio Ramos                Spain
9                       J. Oblak             Slovenia
10                R. Lewandowski               Poland
11                      T. Kroos              Germany
12                      D. Godín              Uruguay
13                   David Silva                Spain
14                      N. Kanté               France
15                     P. Dybala            Argentina
16                       H. Kane              England
17                  A. Griezmann               France
18                 M. ter Stegen              Germany
19                   T. Courtois              Belgium
20               Sergio Busquets                Spain
21                     E. Cavani              Uruguay
22                      M. Neuer              Germany
23                     S. Agüero            Argentina
24                  G. Chiellini                Italy
25                     K. Mbappé               France
26                      M. Salah                Egypt
27                      Casemiro               Brazil
28                  J. Rodríguez             Colombia
29                    L. Insigne                Italy
...                          ...                  ...
18177                  R. Roache  Republic of Ireland
18178               L. Wahlstedt               Sweden
18179                J. Williams              England
18180                   M. Hurst             Scotland
18181                   C. Maher  Republic of Ireland
18182                    Y. Góez             Colombia
18183              K. Pilkington              England
18184                  D. Horton              England
18185                   E. Tweed  Republic of Ireland
18186               Zhang Yufeng             China PR
18187                  C. Ehlich              Germany
18188                 L. Collins                Wales
18189                 A. Kaltner              Germany
18190                 L. Watkins              England
18191       J. Norville-Williams              England
18192                  S. Squire              England
18193                 N. Fuentes                Chile
18194                   J. Milli                Italy
18195                 S. Griffin  Republic of Ireland
18196                K. Fujikawa                Japan
18197                 D. Holland  Republic of Ireland
18198                 J. Livesey              England
18199               M. Baldisimo               Canada
18200                   J. Young             Scotland
18201                   D. Walsh  Republic of Ireland
18202               J. Lundstram              England
18203         N. Christoffersson               Sweden
18204                  B. Worman              England
18205             D. Walker-Rice              England
18206                  G. Nugent              England

[18207 rows x 2 columns]
>>> 
	       
>>> print(type(data["Nationality"]))
	       
<class 'pandas.core.series.Series'>
>>> print(type(data[["Nationality"]]))
	       
<class 'pandas.core.frame.DataFrame'>
>>> 
	       
>>> data.loc[1:10, "Name":"Potential"]
	       
                         Name  Age  ... Overall Potential
Unnamed: 0                          ...                  
1           Cristiano Ronaldo   33  ...      94        94
2                   Neymar Jr   26  ...      92        93
3                      De Gea   27  ...      91        93
4                K. De Bruyne   27  ...      91        92
5                   E. Hazard   27  ...      91        91
6                   L. Modrić   32  ...      91        91
7                   L. Suárez   31  ...      91        91
8                Sergio Ramos   32  ...      91        91
9                    J. Oblak   25  ...      90        93
10             R. Lewandowski   29  ...      90        90

[10 rows x 7 columns]
>>> 
	       
>>> 
	       

>>> 
	       
>>> 
	       
>>> data.loc[10:1:-1, "Name" : "Potential"]
	       
                         Name  Age  ... Overall Potential
Unnamed: 0                          ...                  
10             R. Lewandowski   29  ...      90        90
9                    J. Oblak   25  ...      90        93
8                Sergio Ramos   32  ...      91        91
7                   L. Suárez   31  ...      91        91
6                   L. Modrić   32  ...      91        91
5                   E. Hazard   27  ...      91        91
4                K. De Bruyne   27  ...      91        92
3                      De Gea   27  ...      91        93
2                   Neymar Jr   26  ...      92        93
1           Cristiano Ronaldo   33  ...      94        94

[10 rows x 7 columns]
>>> 
	       
>>> 
	       
>>> data.loc[1:10, "SlidingTackle"]
	       
Unnamed: 0
1     23.0
2     33.0
3     13.0
4     51.0
5     22.0
6     73.0
7     38.0
8     91.0
9     18.0
10    19.0
Name: SlidingTackle, dtype: float64
>>> data.loc[1:10, "SlidingTackle":]
	       
            SlidingTackle  GKDiving  ...  GKReflexes  Release Clause
Unnamed: 0                           ...                            
1                    23.0       7.0  ...        11.0         €127.1M
2                    33.0       9.0  ...        11.0         €228.1M
3                    13.0      90.0  ...        94.0         €138.6M
4                    51.0      15.0  ...        13.0         €196.4M
5                    22.0      11.0  ...         8.0         €172.1M
6                    73.0      13.0  ...         9.0         €137.4M
7                    38.0      27.0  ...        37.0           €164M
8                    91.0      11.0  ...        11.0         €104.6M
9                    18.0      86.0  ...        89.0         €144.5M
10                   19.0      15.0  ...        10.0         €127.1M

[10 rows x 7 columns]
>>> 
	       
>>> 
	       
>>> 
	       
>>> boolean = data.Club =='Juventus'
	       
>>> data[boolean]
	       
                ID               Name  ...  GKReflexes Release Clause
Unnamed: 0                             ...                           
1            20801  Cristiano Ronaldo  ...        11.0        €127.1M
15          211110          P. Dybala  ...         8.0        €153.5M
24          138956       G. Chiellini  ...         3.0         €44.6M
64          191043        Alex Sandro  ...         5.0         €60.2M
65          190483      Douglas Costa  ...         5.0         €76.7M
70          184344         L. Bonucci  ...         4.0         €49.5M
72          180206          M. Pjanić  ...         8.0         €72.6M
73          177509         M. Benatia  ...        11.0         €49.5M
92          186153        W. Szczęsny  ...        87.0         €55.2M
99          179846         S. Khedira  ...         8.0         €54.5M
103         170890         B. Matuidi  ...        14.0         €42.9M
128         198009           M. Perin  ...        90.0         €50.9M
129         193082        J. Cuadrado  ...         9.0         €48.7M
139         181783       M. Mandžukić  ...        15.0         €41.3M
152         137186        A. Barzagli  ...         4.0          €6.9M
243         212404    F. Bernardeschi  ...        12.0         €50.9M
245         211320          D. Rugani  ...         5.0         €42.3M
247         210514       João Cancelo  ...        14.0         €47.2M
448         208333             E. Can  ...        11.0         €33.6M
815         206058      M. De Sciglio  ...         3.0         €18.1M
1049        202884      L. Spinazzola  ...        14.0           €19M
1149        227535       R. Bentancur  ...        12.0         €28.7M
3418        236610            M. Kean  ...         9.0         €14.8M
3700        189342       C. Pinsoglio  ...        76.0          €3.6M
13896       245491        P. Beruatto  ...        12.0          €1.3M

[25 rows x 88 columns]
>>> 
	       
>>> 
	       
>>> 
	       
>>> first_filter = data.Club == 'Juventus'
	       
>>> second_filter = data.Potential >88
	       
>>> dara[first_filter & second_filter]
	       
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    dara[first_filter & second_filter]
NameError: name 'dara' is not defined
>>> data[first_filter &second_filter]
	       
                ID               Name  ...  GKReflexes Release Clause
Unnamed: 0                             ...                           
1            20801  Cristiano Ronaldo  ...        11.0        €127.1M
15          211110          P. Dybala  ...         8.0        €153.5M
24          138956       G. Chiellini  ...         3.0         €44.6M
128         198009           M. Perin  ...        90.0         €50.9M
1149        227535       R. Bentancur  ...        12.0         €28.7M

[5 rows x 88 columns]
>>> 
	       
>>> data.Age[data.Overall>90]
	       
Unnamed: 0
0    31
1    33
2    26
3    27
4    27
5    27
6    32
7    31
8    32
Name: Age, dtype: int64
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> def div(n):
	       return n/2

	       
>>> data.Overall.apply(div)
	       
Unnamed: 0
0        47.0
1        47.0
2        46.0
3        45.5
4        45.5
5        45.5
6        45.5
7        45.5
8        45.5
9        45.0
10       45.0
11       45.0
12       45.0
13       45.0
14       44.5
15       44.5
16       44.5
17       44.5
18       44.5
19       44.5
20       44.5
21       44.5
22       44.5
23       44.5
24       44.5
25       44.0
26       44.0
27       44.0
28       44.0
29       44.0
         ... 
18177    24.0
18178    24.0
18179    24.0
18180    24.0
18181    24.0
18182    24.0
18183    24.0
18184    24.0
18185    24.0
18186    23.5
18187    23.5
18188    23.5
18189    23.5
18190    23.5
18191    23.5
18192    23.5
18193    23.5
18194    23.5
18195    23.5
18196    23.5
18197    23.5
18198    23.5
18199    23.5
18200    23.5
18201    23.5
18202    23.5
18203    23.5
18204    23.5
18205    23.5
18206    23.0
Name: Overall, Length: 18207, dtype: float64
>>> 
	       
>>> 
	       
>>> data.Overall.apply(lamda n : n/2)
	       
SyntaxError: invalid syntax
>>> data.Overall.apply(lambda n : n/2)
	       
Unnamed: 0
0        47.0
1        47.0
2        46.0
3        45.5
4        45.5
5        45.5
6        45.5
7        45.5
8        45.5
9        45.0
10       45.0
11       45.0
12       45.0
13       45.0
14       44.5
15       44.5
16       44.5
17       44.5
18       44.5
19       44.5
20       44.5
21       44.5
22       44.5
23       44.5
24       44.5
25       44.0
26       44.0
27       44.0
28       44.0
29       44.0
         ... 
18177    24.0
18178    24.0
18179    24.0
18180    24.0
18181    24.0
18182    24.0
18183    24.0
18184    24.0
18185    24.0
18186    23.5
18187    23.5
18188    23.5
18189    23.5
18190    23.5
18191    23.5
18192    23.5
18193    23.5
18194    23.5
18195    23.5
18196    23.5
18197    23.5
18198    23.5
18199    23.5
18200    23.5
18201    23.5
18202    23.5
18203    23.5
18204    23.5
18205    23.5
18206    23.0
Name: Overall, Length: 18207, dtype: float64
>>> 
	       
>>> 
	       
>>> data["total_power"] = data.Overall + data.Potential
	       
>>> data.hed()
	       
Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    data.hed()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 5067, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'hed'
>>> data.head()
	       
                ID               Name  ...  Release Clause total_power
Unnamed: 0                             ...                            
0           158023           L. Messi  ...         €226.5M         188
1            20801  Cristiano Ronaldo  ...         €127.1M         188
2           190871          Neymar Jr  ...         €228.1M         185
3           193080             De Gea  ...         €138.6M         184
4           192985       K. De Bruyne  ...         €196.4M         183

[5 rows x 89 columns]
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> print(data.index.name)
	       
Unnamed: 0
>>> data.index.name = "index_name"
	       
>>> data.head()
	       
                ID               Name  ...  Release Clause total_power
index_name                             ...                            
0           158023           L. Messi  ...         €226.5M         188
1            20801  Cristiano Ronaldo  ...         €127.1M         188
2           190871          Neymar Jr  ...         €228.1M         185
3           193080             De Gea  ...         €138.6M         184
4           192985       K. De Bruyne  ...         €196.4M         183

[5 rows x 89 columns]
>>> [5 rows x 89 columns]
	       
SyntaxError: invalid syntax
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> data.head()
	       
                ID               Name  ...  Release Clause total_power
index_name                             ...                            
0           158023           L. Messi  ...         €226.5M         188
1            20801  Cristiano Ronaldo  ...         €127.1M         188
2           190871          Neymar Jr  ...         €228.1M         185
3           193080             De Gea  ...         €138.6M         184
4           192985       K. De Bruyne  ...         €196.4M         183

[5 rows x 89 columns]
>>> data3 = data.copy()
	       
>>> data3.index = range(300,18507,1)
	       
>>> data3.head()
	       
         ID               Name  Age  ... GKReflexes Release Clause total_power
300  158023           L. Messi   31  ...        8.0        €226.5M         188
301   20801  Cristiano Ronaldo   33  ...       11.0        €127.1M         188
302  190871          Neymar Jr   26  ...       11.0        €228.1M         185
303  193080             De Gea   27  ...       94.0        €138.6M         184
304  192985       K. De Bruyne   27  ...       13.0        €196.4M         183

[5 rows x 89 columns]
>>> 
	       
>>> 
	       
>>> 
	       
>>> data = pd.read_csv('/users/ashokpaliwal/DESKTOP/DATA-SCIENCE/Projects/fifa19/fifa19.csv')
	       
>>> data.head()
	       
   Unnamed: 0      ID  ... GKReflexes  Release Clause
0           0  158023  ...        8.0         €226.5M
1           1   20801  ...       11.0         €127.1M
2           2  190871  ...       11.0         €228.1M
3           3  193080  ...       94.0         €138.6M
4           4  192985  ...       13.0         €196.4M

[5 rows x 89 columns]
>>> 
	       
>>> 
	       
>>> data1 = data.set_index(["Name", "Age"])
	       
>>> data1.head()
	       
                       Unnamed: 0      ID  ... GKReflexes Release Clause
Name              Age                      ...                          
L. Messi          31            0  158023  ...        8.0        €226.5M
Cristiano Ronaldo 33            1   20801  ...       11.0        €127.1M
Neymar Jr         26            2  190871  ...       11.0        €228.1M
De Gea            27            3  193080  ...       94.0        €138.6M
K. De Bruyne      27            4  192985  ...       13.0        €196.4M

[5 rows x 87 columns]
>>> 
	       
>>> 
	       
>>> dic = {"teams":["A","A","B","B"], "players":["cris","thomas","bale","mbap"], "response":[10,45,5,9],"age":[22,23,27,19] }
	       
>>> df = pd.DataFrame(dic)
	       
>>> df
	       
  teams players  response  age
0     A    cris        10   22
1     A  thomas        45   23
2     B    bale         5   27
3     B    mbap         9   19
>>> 
	       
>>> 
	       
>>> 
	       
>>> df.pivot(index = "teams", columns = "players", values = "response")
	       
players  bale  cris  mbap  thomas
teams                            
A         NaN  10.0   NaN    45.0
B         5.0   NaN   9.0     NaN
>>> 
	       
>>> 
	       
>>> df1 = df.set_index(["teams","players"])
	       
>>> df1
	       
               response  age
teams players               
A     cris           10   22
      thomas         45   23
B     bale            5   27
      mbap            9   19
>>> 
	       
>>> df1.unstack(level = 0)
	       
        response        age      
teams          A    B     A     B
players                          
bale         NaN  5.0   NaN  27.0
cris        10.0  NaN  22.0   NaN
mbap         NaN  9.0   NaN  19.0
thomas      45.0  NaN  23.0   NaN
>>> 
	       
>>> df1.unstack(level = 1)
	       
        response                     age                   
players     bale  cris mbap thomas  bale  cris  mbap thomas
teams                                                      
A            NaN  10.0  NaN   45.0   NaN  22.0   NaN   23.0
B            5.0   NaN  9.0    NaN  27.0   NaN  19.0    NaN
>>> 
	       
>>> df2 = df1.swaplevel(0,1)
	       
>>> df2
	       
               response  age
players teams               
cris    A            10   22
thomas  A            45   23
bale    B             5   27
mbap    B             9   19
>>> 
	       
>>> 
	       
>>> 
	       
>>> df
	       
  teams players  response  age
0     A    cris        10   22
1     A  thomas        45   23
2     B    bale         5   27
3     B    mbap         9   19
>>> 
	       
>>> 
	       
>>> df.melt(df,id_vars="teams",value_vars=["age","response"])
	       
Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    df.melt(df,id_vars="teams",value_vars=["age","response"])
TypeError: melt() got multiple values for argument 'id_vars'
>>> pd.melt(df,id_vars="teams",value_vars=["age","response"])
	       
  teams  variable  value
0     A       age     22
1     A       age     23
2     B       age     27
3     B       age     19
4     A  response     10
5     A  response     45
6     B  response      5
7     B  response      9
>>> 
	       
>>> 
	       
>>> 
	       
>>> df
	       
  teams players  response  age
0     A    cris        10   22
1     A  thomas        45   23
2     B    bale         5   27
3     B    mbap         9   19
>>> 
	       
>>> 
	       
>>> df.groupby("teams").mean()
	       
       response   age
teams                
A          27.5  22.5
B           7.0  23.0
>>> 
	       
>>> df.groupby("teams").age.max()
	       
teams
A    23
B    27
Name: age, dtype: int64
>>> 
	       
>>> df.groupby("temas")[["age","response"]].min()
	       
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    df.groupby("temas")[["age","response"]].min()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 7632, in groupby
    observed=observed, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/groupby/groupby.py", line 2110, in groupby
    return klass(obj, by, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/groupby/groupby.py", line 360, in __init__
    mutated=self.mutated)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/groupby/grouper.py", line 578, in _get_grouper
    raise KeyError(gpr)
KeyError: 'temas'
>>> df.groupby("teams")[["age","response"]].min()
       age  response
teams               
A       22        10
B       19         5
>>> 
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
teams       4 non-null object
players     4 non-null object
response    4 non-null int64
age         4 non-null int64
dtypes: int64(2), object(2)
memory usage: 208.0+ bytes
>>> 
