import pandas as pd
import openpyxl

excel_data = pd.read_excel("post.xlsx")
data = pd.DataFrame(excel_data, columns=["Заголовок поста", "Текст поста", "Категория",	"Тег"])

for val in range(data.shape[0]):
    print(data.values[val])
    for j in range(data.shape[1]):
        print(data.values[val][j])
