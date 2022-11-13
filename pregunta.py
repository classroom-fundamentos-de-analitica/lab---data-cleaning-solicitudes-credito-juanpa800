"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import datetime as dt

def campo_a_minuscula(df,campo):
    df[campo] = df[campo].str.capitalize()
    return df

def borrar_char(df,campo):
    df[campo] = df[campo].str.replace('_',' ')
    df[campo] = df[campo].str.replace('-',' ')
    return df

def clean_data():
    

    df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding='utf8')
    
    # Tenga en cuenta datos faltantes
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    df = campo_a_minuscula(df, 'sexo')
    df = campo_a_minuscula(df, 'tipo_de_emprendimiento')
    df = campo_a_minuscula(df, 'idea_negocio')
    df = campo_a_minuscula(df, 'barrio')
    df = campo_a_minuscula(df,'línea_credito')
    df = borrar_char(df, 'idea_negocio')
    df = borrar_char(df, 'barrio')
    df = borrar_char(df,'línea_credito')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$',"",regex=False)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('.00',"",regex=False)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',',"")
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: dt.datetime.strptime(x, "%d/%m/%Y") if (x[-5] == '/' and x[-8] == '/') else dt.datetime.strptime(x, "%Y/%m/%d"))
    
    # Tenga en cuenta duplicados
    df.drop_duplicates(inplace = True)
    return df
