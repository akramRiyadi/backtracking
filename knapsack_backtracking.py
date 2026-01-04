import pandas as pd


df = pd.read_excel("backtracking.xlsx")
df.columns = df.columns.str.strip()

items = []
weights = []
values = []

for _, row in df.iterrows():
    items.append(str(row["StockCode"]))

    w = row["Quantity"]
    if isinstance(w, (int, float)):
        weights.append(int(w))
    else:
        weights.append(0)

    v = row["Price"]
    if isinstance(v, (int, float)):
        values.append(float(v))
    else:
        values.append(0.0) 

n = len(items)

CAPACITY = 15

max_value = 0
best_solution = [0] * n

def knapsack_backtracking(i, w, v, sol):
    global max_value, best_solution

    if w > CAPACITY:
        return

    if i == n:
        if v > max_value:
            max_value = v    
            best_solution = sol.copy()
        return

    sol[i] = 1
    knapsack_backtracking(
        i + 1,
        w + weights[i],
        v + values[i],
        sol
    )

    sol[i] = 0
    knapsack_backtracking(
        i + 1,
        w,
        v,
        sol
    )

knapsack_backtracking(0, 0, 0, [0] * n)

total_weight = 0
selected_items = []

for i in range(n):
    if best_solution[i] == 1:
        selected_items.append(items[i])
        total_weight += weights[i]

def knapsack_dp(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # tidak ambil item
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # ambil item
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected

dp_max_value, dp_selected_items = knapsack_dp(weights, values, CAPACITY)

print("\nHASIL DYNAMIC PROGRAMMING 0/1 KNAPSACK")
print("Nilai maksimum  :", dp_max_value)
print("Item terpilih   :", dp_selected_items)
print("Kapasitas       :", CAPACITY)

print("\n HASIL BACKTRACKING 0/1 KNAPSACK ")
print("Jumlah item     :", n)
print("Nilai maksimum  :", max_value)
print("Item terpilih   :", selected_items)
print("Total berat     :", total_weight)
print("Kapasitas       :", CAPACITY)
