#Определить какое максимальное и минимальное значение median_house_value
#(Доп) Показать максимальное median_house_value, где median_income = 3.1250
#(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value

# Максимальное и минимальное
max_mhv = c_h_t['median_house_value'].max()
min_mhv = c_h_t['median_house_value'].min()
print(f"Максимальное значение = {max_mhv},\nМинимальное значение =  {min_mhv}")
Максимальное значение = 500001.0,
Минимальное значение =  22500.0
# Доп_1
print(c_h_t.loc[c_h_t['median_income'] == 3.1250, ['median_house_value']].max())
median_house_value    233300.0
dtype: float64
# Доп_2
c_h_t.loc[(c_h_t['median_house_value'] == min_mhv), ['population']].max()
population    1230.0
dtype: float64