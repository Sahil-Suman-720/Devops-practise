import pandas as pd
data = pd.read_excel('./Campus recruitment Training batch 2025 - Technology Nominations for batches.xlsx')
print(data['Select your technology ,you want the training for you'])
count_j = 0
count_p = 0
for ele in  data['Select your technology ,you want the training for you']:
    if ele == "DSA - With Java":
        count_j += 1
    else:
        count_p += 1

print("java : {} ( {} % ) python :{} ( {} % )".format(count_j,(count_j/1140 * 100),count_p,(count_p/1140 * 100)))
