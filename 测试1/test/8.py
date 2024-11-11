from tqdm import tqdm

X = 10000
for i in tqdm(range(X), desc='Progress'):
    for j in range(X):
        k = j * i
print('\n完成!')
