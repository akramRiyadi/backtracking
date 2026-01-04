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

print("\n=== HASIL BACKTRACKING 0/1 KNAPSACK ===")
print("Jumlah item     :", n)
print("Nilai maksimum  :", max_value)
print("Item terpilih   :", selected_items)
print("Total berat     :", total_weight)
print("Kapasitas       :", CAPACITY)
