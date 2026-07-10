categories = int(input("Enter the number of categories: "))
cats={}

for cat in range(categories):
    name = input(f"Enter the category {cat + 1}'s name: ")
    cats[name]={}
    prod = int(input(f"Enter the number of products in {name}: "))

    for i in range(prod):
        item = input(f"Enter the name of product{i+1}: ")
        stock = int(input(f"Enter the stock for {item}: "))
        cats[name][item] = stock

print("===INVENTORY STOCK===")
for cat in cats:
    print(f"Category: {cat}")
    l = cats[cat]
    for i in l:
        print(f"{i} : {l[i]}")