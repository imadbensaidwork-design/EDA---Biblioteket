# Här lägger vi in nyckeltalsfunktioner

import pandas as pd


# TOTALA LÅN

def total_loans(df: pd.DataFrame) -> int: # pd.DataFrame anger att parametern förväntas vara en pandas-DataFrame
    return df["loan_id"].nunique() # .nunique() räknar antalet unika värden (utan dubbletter)

# ANTAL LÅNEDAGAR I GENOMSNITT
def avg_loan_days(df: pd.DataFrame) -> float:
    return float(df["loan_days"].mean())

# FÖRSENINGSKOSTNAD
def overdue_rate(df: pd.DataFrame) -> float:
    return float((df["overdue_days"] > 0).mean()) # De extra parenteserna behövs för att Python 
                                                  # ska behandla villkoret df["overdue_days"] > 0 
                                                  # som en hel operation innan .mean() körs.

# LÅN PER GENRE
def loans_by_genre(df: pd.DataFrame) -> pd.DataFrame: # vi talar om att vi kommer skicka funktionen en df, och att den kommer returnera en df
    """
    Delar upp raderna per genre och räknar lån i varje grupp
    """
    return (
        df.groupby("genre", dropna=False)["loan_id"] # dropna=False gör att även rader där genre saknas (NaN) får en egen grupp # OBS: Raderna tas inte bort från den ursprungliga DataFrame:en
        .nunique() # .nunique() (kopplad till "loan_id") räknar antalet unika värden (utan dubbletter)   
        # groupby: samlar alla lån med en genren i en grupp. Sedan räknar .nunique() hur många unika lån som finns i just den gruppen                       
        .sort_values(ascending=False) # visar högst värden först (genrer med flest antal lån)
    )   .reset_index(name="loans") # Gör om resultatet från en Series till en DataFrame. Flyttar genre från index till en vanlig kolumn. Döp­er kolumnen med antalet lån till "loans"
        # Gör om resultatet från en Series till en DataFrame
        # genre blir en vanlig kolumn istället för index
        # loans blir namnet på kolumnen med antal lån

def loans_by_branch(df: pd.DataFrame) -> pd.DataFrame:
    """
    Delar upp raderna per branch (filial) och räknar lån i varje grupp
    """
    return (
        df.groupby("branch", dropna=False)["loan_id"] # gruppera enligt branch
        .nunique() # nunique (kopplad till loan_id) räknar antalet unika värden
        .sort_values(ascending=False) # i fallande ordning (stigning=falsk)
        .reset_index(name="loans") # flyttar branch från index till vanlig kolumn
    )