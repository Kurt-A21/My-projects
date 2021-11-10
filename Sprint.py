import pandas as pd

df = pd.DataFrame([("Simba", "Coke", "Cadbury", "Pepper Steak", "Pear", "Vanilla", "Spinach"),
                   ("Lays", "Fanta", "Tex", "Chicken", "Apple", "Chocolate", "Cabbage")],
            columns=("Chips", "Cooldrinks", "Chocolate", "Pies", "Fruit", "Cupcakes", "Veggies")
                    )
df2 = pd.DataFrame([("", "", "", "", "Orange", "", "")],
            columns=("Chips", "Cooldrinks", "Chocolate", "Pies", "Fruit", "Cupcakes", "Veggies")
                    )

df = df.append(df2, ignore_index=True, sort = False) 

print(df)