import pandas as pd
# import numpy as np
import json

#Read the Excel for column
file_loc = "VueLocale.xlsx"

#Select Index(Code) and Column of Language
den = pd.read_excel(file_loc,index_col="code", usecols = "A,C,D")
print(den)

#Turn the Data into JSON array
result = den.to_json(orient="columns")
parsed = json.loads(result)

#Save the Language JSON according the the locale(Key)
for key, value in parsed.items():
    datas = json.dumps(value, indent=4, separators=(", ", " : "))
    with open(str(key)+'.json', 'w+') as j:
        print(datas, file=j)


#Once you done this can save that 2 json it to Vue Project/src/locales
