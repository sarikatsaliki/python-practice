#list of dictionaries named expenses
expenses = [
    {"name": "pizza", "amount":300, "category":"food"},
    {"name": "cab", "amount": 2000, "category": "transport"},
    {"name":"shoes","amount": 4000, "category": "shopping" },
    {"name": "rent", "amount": 10000, "category":"expenditure"}
]
total_sum = 0
max_item = expenses[0]
# loop that calculates the total_sum.
for item in expenses:
    total_sum += item["amount"]
#names of expenses where amount > 50
    if item["amount"]> max_item["amount"]:
     max_item = item
print(total_sum)
print(max_item)
