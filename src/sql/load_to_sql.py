from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer
import pandas as pd

def load_data_to_sql():
    # Load cleaned dataset from csv
    cleaned_data = pd.read_csv('../data/processed/cleaned_happiness_data.csv')

    # Define the schema
    metadata = MetaData()
    data_table = Table(
        'cleaned_data',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('Score', Float),
        Column('GDPperCapita', Float),
        Column('Family', Float),
        Column('LifeExpectancy', Float),
        Column('Freedom', Float),
        Column('NoCorruption', Float),
        Column('Generosity', Float),
        Column('DystopiaResidual', Float),
        Column('HappinessIndicator', Integer)
    )

    # Create the sqlalchemy engine
    engine = create_engine('sqlite:///happiness_data.sqlite', echo=False)

    # Create the table in the database
    metadata.create_all(engine)

    # Save the dataframe to the sql database
    cleaned_data.to_sql('happiness_data', con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    load_data_to_sql()