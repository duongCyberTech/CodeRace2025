from cantools.database import load_file
import pandas as pd
import csv

# Load file DBC
db = load_file('./BOSCH_CAN Data.dbc')

# Danh sách chứa từng dòng dữ liệu
rows = []

for msg in db.messages:
    print(f"Processing message: {msg.name} (ID: {hex(msg.frame_id)}) -- {len(msg.signals)} signals")
    for sig in msg.signals:
        enum_text = "; ".join(f"{k}: {v}" for k, v in (sig.choices or {}).items())
        rows.append({
            "Message": msg.name,
            "ID": hex(msg.frame_id),
            "CycleTime": msg.cycle_time,
            "DLC": msg.length,
            "Signal": sig.name,
            "StartBit": sig.start,
            "Length": sig.length,
            "Endianess": "Intel" if sig.byte_order == "little_endian" else "Motorola",
            "Signed": sig.is_signed,
            "Factor": sig.scale,
            "Offset": sig.offset,
            "Min": sig.minimum,
            "Max": sig.maximum,
            "Unit": sig.unit,
            "Enum (ValueTable)": enum_text,
            "Initial Value": sig.initial,
            "Comment": sig.comment
        })


df = pd.DataFrame(rows)
print(df)
df.to_csv("signals_summary.csv", index=False, encoding="utf-8-sig")


