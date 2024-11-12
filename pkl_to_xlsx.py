import pandas as pd
import pickle
# # Load model weights
# model_weights = torch.load('E:/Epan/data/Human_features/processed/1A0N.pt')
# model_weights1 = model_weights


with open('E:/Epan/MFEPre/dataset/74_encode_data.pkl','rb') as file:
    content = pickle.load(file)


# all_data = pd.DataFrame()
#

# for ndarray in content:
#     df = pd.DataFrame(ndarray)
#     all_data = pd.concat([all_data, df], ignore_index=True)
#
# excel_path = 'E:/Epan/data/Human_features/combined_data.xlsx'
# all_data.to_excel(excel_path, index=False)
#
# print(f"All data has been successfully saved to {excel'path}")

for index, ndarray in enumerate(content, start=1):

    df = pd.DataFrame(ndarray)

    excel_path = f'E:/Epan/MFEPre/dataset/excel_{index}.xlsx'

    df.to_excel(excel_path, index=False)

    print(f"The data for list {index} has been successfully saved to {excel'path}")
