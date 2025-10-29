import io
import pandas as pd
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LISR
# ------------------------------------------------------------

data = {
    "theme": [
        "cross_joins",
        "cross_joins",
        "window_functions",
        "window_functions",
        "window_functions",
        "window_functions",
        "window_functions",
        "window_functions",
    ],
    "exercise_name": [
        "beverages_and_food",
        "sizes_and_trademarks",
        "window_functions_1",
        "window_functions_2",
        "window_functions_3",
        "window_functions_4",
        "window_functions_5",
        "window_functions_6",
    ],
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
        ["furniture"],
        ["furniture"],
        ["furniture"],
        ["capteur_a_retrail"],
        ["capteur_a_retrail"],
        ["capteur_a_retrail"],
    ],
    "last_reviewed": [
        "1980-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
        "1970-01-01",
    ],
    "question": [
        "question 1",
        "question 2",
        "Display the total weight in a new column",
        "Display the running total weight in a new column",
        "Display the moving average weight in a new column",
        "Display the total visitor in a new column",
        "Display the running total visitor in a new column",
        "Display the moving average visitor for the last 7 days in a new column",
    ],
}
memory_state_df = pd.DataFrame(data)
con.execute(
    "CREATE TABLE IF NOT EXISTS memory_state_df AS SELECT * FROM memory_state_df"
)

# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

# ------------------------------------------------------------
# WINDOW FUNCTIONS EXERCISES
# ------------------------------------------------------------
furniture = [
    ("Chairs", "Chair 1", 5.2),
    ("Chairs", "Chair 2", 4.5),
    ("Chairs", "Chair 3", 6.8),
    ("Sofas", "Sofa 1", 25.5),
    ("Sofas", "Sofa 2", 20.3),
    ("Sofas", "Sofa 3", 30.0),
    ("Tables", "Table 1", 15.0),
    ("Tables", "Table 2", 12.5),
    ("Tables", "Table 3", 18.2),
]
furniture = pd.DataFrame(furniture, columns=["category", "item", "weight"])
con.execute("CREATE TABLE IF NOT EXISTS furniture AS SELECT * FROM furniture")

capteur_a_retrail = pd.read_csv("data_csv/capteur_a_retrail.csv")
con.execute(
    "CREATE TABLE IF NOT EXISTS capteur_a_retrail AS SELECT * FROM capteur_a_retrail"
)

con.close()
