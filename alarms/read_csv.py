import pandas as pd


# making dataframe

def csv_to_df():

    filepath = "RepGeneral_20221206141603.csv"
    df = pd.read_csv(filepath, sep=';', header=None)
    # output the dataframe

    clients_df = pd.DataFrame()
    clients_df['name'] = [i for i in df[28]]
    clients_df['date'] = [i for i in df[2]]
    clients_df['phone_number'] = [str(i) for i in df[32]]
    clients_df['email'] = [i for i in df[41]]
    clients_df['car_id'] = [i for i in df[10]]
    clients_df['brand'] = [i for i in df[12]]
    clients_df['line'] = [i for i in df[13]]
    clients_df

    clients_df.to_csv('testing_a.csv')

csv_to_df()