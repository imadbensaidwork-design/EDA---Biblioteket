import pandas as pd

# FUNKTION 1: LÄSER IN CSV-FILER, OCH RETURNERAR DATAFRAME

REQUIRED = [ # lista med kolumner som måste finnas i CSV-filen - REQUIRED är en konstant
    "loan_id", "checkout_date", 
    "branch", "genre", "item_type", 
    "patron_age_group", "patron_age", 
    "returned_date", "overdue_days", 
    "fine_amount"
]
            # path gör funktionen flexibel, eftersom du kan skicka in olika sökvägar utan att ändra själva funktionen.
def load_data(path: str) -> pd.DataFrame: # förklarar att den här kommer ge tillbaka en DataFrame
    """ 
    Läser CSV och gör datumkolumner till datetime
    """
    df = pd.read_csv(path, parse_dates=["checkout_date", "returned_date"]) # parse_dates= läser in date-kolumner i csv-filen som datetime[us]
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"saknade kolumner: {missing}") # missing sparar kolumnnamnen om de inte finns df.colmuns, från vår DataFrame (som lästs in från en csv-fil)
    return df # returnerar en DataFrame

# FUNKTION 2: 

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Säkerställer att numeriska kolumner faktiskt är numeriska
    """
    out = df.copy() # kopierar först originaldata, så vi inte manipulerar orginaldata
    for c in ["overdue_days", "fine_amount"]: # itererar genom listan med kolummer
        out[c] = pd.to_numeric(out[c], errors="coerce") # konverterar kolumnen i kopian out till numeriska värden och ersätter värden som inte kan konverteras med NaN
    return out # returnerar kopian out