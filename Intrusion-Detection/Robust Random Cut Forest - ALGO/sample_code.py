# Docs: https://github.com/kLabUM/rrcf
# Site: https://klabum.github.io/rrcf/


def create_tree():
    tree = rrcf.RCTree()
    idx = 0
    for i in X_train.values:
        _ = tree.insert_point(i, index=idx)
        idx += 1
    return tree


tree = create_tree()
type(tree)

# codisp_list = [tree.codisp(leaf) for leaf in tree.leaves] # so i dont
# have to (ab)use index naming
codisp = np.vectorize(lambda x: tree.codisp(x))
codisp_list = codisp(np.arange(length))


def gen_tree(num_trees):
    # Set parameters
    n = X_train.shape[0]
    num_trees = 20

    # Construct forest
    forest = []
    while len(forest) < num_trees:
        tree = rrcf.RCTree()
        idx = 0
        for i in X_train.values:
            _ = tree.insert_point(i, index=idx)
            idx += 1
        forest.append(tree)

    # Compute average CoDisp
    avg_codisp = pd.Series(0.0, index=np.arange(n))
    index = np.zeros(n)
    for tree in forest:
        codisp = pd.Series({leaf: tree.codisp(leaf) for leaf in tree.leaves})
        avg_codisp[codisp.index] += codisp
        np.add.at(index, codisp.index.values, 1)
    avg_codisp /= index
    return avg_codisp.round(2)


# o =    gen_tree(num_trees = 1)
# t =    gen_tree(num_trees = 3)
# f =    gen_tree(num_trees = 5)
# ten =  gen_tree(num_trees = 10)
# fif =  gen_tree(num_trees = 15)
# tw =   gen_tree(num_trees = 20)
# [o,t,f,ten,fif,tw]
df_compare = pd.DataFrame(gen_tree(num_trees=5))
print("Trees made; Data saved is `df_compare`")


# np.var(gen_tree(num_trees = 1)[70:])
# 212.05 or 188.41 (subject to seed/chance)
# exclude first 70: 15.61 or 12.86
# np.var(gen_tree(num_trees = 25)[70:])
# 247.37885271110034
# exclude first 70:  12.13

data = df_compare[0][70:].values

print("Mean: ", np.mean(data))
print("Max: ", np.max(data))
print("Min: ", np.min(data))
print("Median: ", np.median(data))

np.mean(data)
np.std(data)

np.mean(residual)
np.std(residual)


def moving_average(a, n=7):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return np.concatenate((np.zeros(n - 1), ret[n - 1:] / n))

# data[300] = 200 @ allighment testing


# _ = plt.figure(figsize=(32,8))
# plt.plot(data, label = 'data')              # Data
# plt.plot(moving_average(data , 5))          # Moving average
# plt.plot([np.mean(data)] * len(data), 'g-') # Average

moving_avg = 7
residual = np.abs(data - moving_average(data, moving_avg))

size = 250
eq = np.mean(residual[250:]) + 0.75 * np.std(residual[250:]) < residual

for i in range(size):
    if i < 25:
        eq[i] = False
    else:
        eq[i] = (np.mean(residual[:size]) + 0.75 *
                 np.std(residual[:size]) < residual[i])

for i in range(len(eq)):  # 0.75 or 0.9
    if eq[i]:
        _ = plt.axvline(i, color='k', alpha=0.2)

_ = plt.plot(residual, label='residual')       # Data - Moving average
_ = plt.plot([np.mean(residual) + 0.75 * np.std(residual)] *
             len(data), 'g-', alpha=0.8, label='Threshold')
_ = plt.legend()


plt.figure(figsize=(32, 4))
idx = 0
for i in data > 2 * np.mean(data):
    if i:
        _ = plt.axvline(idx, color='k', alpha=0.2)
    idx += 1
plt.plot(residual)


plt.figure(figsize=(32, 4))
idx = 0
for i in np.mean(residual) + 0.75 * np.std(residual) < residual:
    if i:
        _ = plt.axvline(idx, color='k', alpha=0.2)
    idx += 1
plt.plot(residual)


# might_be_evil = data[data > 2 * np.mean(data)]
might_be_evil = data[np.mean(residual) + 0.75 * np.std(residual) < residual]


count = len(might_be_evil)
print(count)
print(count / data.shape[0], "%")

top_2_idx = np.argsort(data)[-count:]
top_2_values = X_train.iloc[top_2_idx]  # [data[i] for i in top_2_idx]

inverse_transform_DF(top_2_values).tail(10)


# from minisom import MiniSom
# too hard... https://github.com/JustGlowing/minisom/blob/master/examples/OutliersDetection.ipynb
# som = MiniSom(15, 1, X_train.shape[1], sigma=0.3, learning_rate=0.5) # initialization of 6x6 SOM
# som.train(X_train.values, 10) # trains the SOM with 100 iterations
