import tabula
import pandas as pd
import sys
import os
import re



input_path = r"C:\Users\Akash-SEQ\Desktop\north\2nd.pdf" #path_of_pdf
output_file_name = os.path.basename(input_path).replace(".pdf", ".csv")
output_dir_path = os.path.dirname(input_path)
output_path = output_dir_path + "\\" + output_file_name #path_of_output_csv_file

df = tabula.read_pdf(input_path, pages ='all', stream=True, pandas_options={'header': None})
list_df = []

for idx_number, chuked_df in enumerate(df):
    if isinstance(chuked_df, pd.DataFrame):
        #chuked_df.replace({r'\r': ''} , regex=True)
        list_df.append(chuked_df)

if len(list_df) > 0:
    frame = pd.concat(list_df, axis=0, ignore_index=True)
    frame.to_csv(output_path, encoding='utf-8', index=False, quoting=1)
    print(output_path)
