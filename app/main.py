import pandas as pd
import charts

def get_population(df):
    population_dic={
        '2022' : int(df['2022 Population']),
        '2020' : int(df['2020 Population']),
        '2015' : int(df['2015 Population']),
        '2010' : int(df['2010 Population']),
        '2000' : int(df['2000 Population']),
        '1990' : int(df['1990 Population']),
        '1980' : int(df['1980 Population']),
        '1970' : int(df['1970 Population']),
    }
    
    labels = population_dic.keys()
    values = population_dic.values()
    
    return labels, values

def populatiton_by_country(df, country):
    filtro = df[df['Country/Territory'] == country]
    return filtro


def run():
    path = './world_population.csv'
    df = pd.read_csv(path)    
    
    country = input("Digite un pais a filtrar = > ").lower().capitalize()
    
    result = populatiton_by_country(df, country)
    print(result)
    
    if len(result) > 0:
        country = result.iloc[0]
        labels, values = get_population(country)
        charts.bar_chart(country['Country/Territory'], labels, values)
        
    
if __name__ == '__main__':
    run()