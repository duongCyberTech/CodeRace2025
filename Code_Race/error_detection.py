import pandas as pd
import csv
import cantools

pfile = './p_data/signals_summary_v2.csv'

df = pd.read_csv(pfile, encoding='utf-8-sig', quoting=csv.QUOTE_NONNUMERIC)

# Kiểm tra các signals bị lỗi 
# Các lỗi có thể gặp: _P_ERR_ (LỖI CỐ ĐỊNH), _T_ERR_ (LỖI TẠM THỜI), _ERR_MC (LỖI CHÍNH), _RECEIVE_ERROR_ (LỖI NHẬN), _SEND_ERROR_ (LỖI GỬI)
error_signals = []
for index, row in df.iterrows():
    if 'P_ERR_' in str(row['Signal']):
        error_signals.append({
            "Message": row['Message'],
            "ID": row['ID'],   
            "Signal": row['Signal'],
            "Comment": row['Comment'] if 'Comment' in row else 'No comment',
            "Error Type": "Permanent Error"
        })
    elif 'T_ERR_' in str(row['Signal']):
        error_signals.append({
            "Message": row['Message'],
            "ID": row['ID'],   
            "Signal": row['Signal'],
            "Comment": row['Comment'] if 'Comment' in row else 'No comment',
            "Error Type": "Temporary Error"
        })
    elif 'ERR_MC' in str(row['Signal']):
        error_signals.append({
            "Message": row['Message'],
            "ID": row['ID'],   
            "Signal": row['Signal'],
            "Comment": row['Comment'] if 'Comment' in row else 'No comment',
            "Error Type": "Main Error"
        })
    elif 'RECEIVE_ERROR' in str(row['Signal']):
        error_signals.append({
            "Message": row['Message'],
            "ID": row['ID'],   
            "Signal": row['Signal'],
            "Comment": row['Comment'] if 'Comment' in row else 'No comment',
            "Error Type": "Receive Error"
        })
    elif 'SEND_ERROR' in str(row['Signal']):
        error_signals.append({
            "Message": row['Message'],
            "ID": row['ID'],   
            "Signal": row['Signal'],
            "Comment": row['Comment'] if 'Comment' in row else 'No comment',
            "Error Type": "Send Error"
        })

if error_signals:
    print("Các signals có lỗi:")
    for error in error_signals:
        print(f"Message: {error['Message']}, Signal: {error['Signal']}, Comment: {error['Comment']}, Error Type: {error['Error Type']}")
else:
    print("Không có signals nào có lỗi.")

# Lưu kết quả vào file CSV
error_df = pd.DataFrame(error_signals)
if not error_df.empty:
    error_df.to_csv("./p_data/error_signals_summary.csv", index=False, encoding="utf-8-sig", quoting=csv.QUOTE_NONNUMERIC)
    print("Kết quả đã được lưu vào file error_signals_summary.csv")
