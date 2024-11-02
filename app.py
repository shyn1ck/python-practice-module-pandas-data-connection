import pandas as pd

file1_path = '/Users/parvizjon/python-practicу-module-pandas-data-connection/python-practicу-module-pandas-data-connection/accounts_more_info.xlsx'
file2_path = '/Users/parvizjon/python-practicу-module-pandas-data-connection/python-practicу-module-pandas-data-connection/accounts_card_info.xlsx'

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

print("Данные из accounts_more_info.xlsx:")
print(df1.head())

print("\nДанные из accounts_card_info.xlsx:")
print(df2.head())

df1.columns = ['id', 'balance', 'currency']

df2.columns = ['id', 'customer_id', 'account_type', 'card_type']

merged_df = pd.merge(df1, df2, on='id')
print("\nОбъединённый DataFrame по столбцу 'id':")
print(merged_df)

data3 = {
    'id': [1, 2, 3, 4, 5],
    'bonus': [500, 700, 450, 600, 800],
    'year': [2023, 2023, 2023, 2023, 2023]
}
df3 = pd.DataFrame(data3)
print("\nТретий DataFrame df3:")
print(df3)

concat_df = pd.concat([merged_df, df3], axis=0, ignore_index=True)
print("\nКонкатенированный DataFrame по оси 0:")
print(concat_df)
