import os
import logging
import streamlit as st
import duckdb
from datetime import date, timedelta, datetime

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python", "init_db.py"]) doesn't work well on streamlit

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


def check_users_solution(user_query: str) -> None:
    """
    Checks that user SQL query is correct by:
    1: Checking the columns
    2: Checking the values
    :param user_query: a string containing the query written by the user
    """
    result = con.execute(query).df()
    st.dataframe(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
        if result.compare(solution_df).shape == (0, 0):
            st.write("Correct!")
            st.balloons()
    except KeyError as e:
        st.write("Some columns are missing")
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution_df"
        )


with st.sidebar:
    available_theme_df = con.execute("SELECT DISTINCT theme FROM memory_state_df").df()
    theme = st.selectbox(
        "What would you like to review?",
        available_theme_df["theme"].unique(),
        index=None,
        placeholder="Select a theme ...",
    )
    if theme:
        st.write("You selected", theme)
        select_exercise_query = f"SELECT * FROM memory_state_df WHERE theme = '{theme}'"
    else:
        select_exercise_query = f"SELECT * FROM memory_state_df"
    exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    solution_df = con.execute(answer).df()

st.header("Enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")

if query:
    check_users_solution(query)

for n_days in [2, 7, 21]:
    if st.button(f"Revoir dans {n_days} jours"):
        next_review = date.today() + timedelta(days=n_days)
        con.execute(
            f"UPDATE memory_state_df SET last_reviewed = '{next_review}' WHERE exercise_name= '{exercise_name}'"
        )
        st.rerun()

if st.button("Reset"):
    con.execute(f"UPDATE memory_state_df SET last_reviewed = '1970-01-01'")
    st.rerun()

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)
