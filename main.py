import pandas as pd
from sendMail import sendMail

sheets_dict = pd.read_excel('Thông báo.xlsx', sheet_name=None, engine='openpyxl')

for sheet_name, df_sheet in sheets_dict.items():
    df_sheet = df_sheet.dropna(axis=1, how='all')
    
    print(f"Sheet: {sheet_name}")
    
    print("\nNhững người đã Đậu:")
    nguoi_dau = df_sheet[df_sheet['KẾT QUẢ'] == 'Đậu']
    for index, row in nguoi_dau.iterrows():
        if pd.notna(row['MAIL']) and pd.notna(row['HỌ TÊN']):
            print(f"HỌ TÊN: {row['HỌ TÊN']}, MAIL: {row['MAIL']} ----------- Đậu")
            sendMail(row['MAIL'], row['HỌ TÊN'], True)
        else:
            print(f"HỌ TÊN: {row['HỌ TÊN']} không có thông tin, bỏ qua việc gửi email.")
    print(f"\nTổng số người đã đậu: {len(nguoi_dau)}")
    print("\nNhững người đã rớt:")
    nguoi_truot = df_sheet[df_sheet['KẾT QUẢ'] == 'Rớt']
    for index, row in nguoi_truot.iterrows():
        if pd.notna(row['MAIL']) and pd.notna(row['HỌ TÊN']) :
            print(f"HỌ TÊN: {row['HỌ TÊN']}, MAIL: {row['MAIL']} ------------ Rớt")
            sendMail(row['MAIL'], row['HỌ TÊN'], False)
        else:
            print(f"HỌ TÊN: {row['HỌ TÊN']} không có thông tin, bỏ qua việc gửi email.")
    print(f"\nTổng số người đã rớt: {len(nguoi_truot)}")
