# Här lägger vi in nyckeltalsfunktioner

import pandas as pd


# NAMN PÅ FUNKTION

def total_loans(df: pd.DataFrame) -> int: # pd.DataFrame anger att parametern förväntas vara en pandas-DataFrame
    return df["loan_id"].nunique() # .nunique() räknar antalet unika värden (utan dubbletter)


def avg_loan_days(df: pd.DataFrame) -> float:
    return float(df["loan_days"].mean())


def overdue_rate(df: pd.DataFrame) -> float:
    return float((df["overdue_days"] > 0).mean()) # De extra parenteserna behövs för att Python 
                                                  # ska behandla villkoret df["overdue_days"] > 0 
                                                  # som en hel operation innan .mean() körs.