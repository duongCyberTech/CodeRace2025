import cantools
import pandas as pd
import csv
import googletrans as gt
import asyncio

def safe_translate(text):
    try:
        return asyncio.run(translator.translate(text, src='ja', dest='en')).text
    except Exception as e:
        print(f"[Translation failed]: {text} -> {e}")
        return text

translator = gt.Translator()
dbc_file = './raw_data/BOSCH_CAN Data.dbc'
db = cantools.database.load_file(dbc_file, encoding='shift_jis')
rows = []
txt_file = './p_data/msg.txt'

for msg in db.messages:
    print(f"{msg}")
    with open(txt_file, 'a', encoding='utf-8-sig') as f:
        f.write(f"{msg}\n")
    for sig in msg.signals:
        print(f"-- {sig}")
        with open(txt_file, 'a', encoding='utf-8-sig') as f:
            f.write(f"-- {sig}\n")
        enum_table = "; ".join(f"{k}: {safe_translate(v)}" for k, v in (sig.choices or {}).items())
        rows.append({
            "Message": msg.name,
            "ID": hex(msg.frame_id),
            "CycleTime": msg.cycle_time,
            "DLC": msg.length,
            "Signal": sig.name,
            "StartBit": sig.start,
            "Length": sig.length,
            "Endianess": sig.byte_order,
            "Signed": sig.is_signed,
            "Factor": sig.scale,
            "Offset": sig.offset,
            "Min": sig.minimum,
            "Max": sig.maximum,
            "Unit": sig.unit,
            "Enum (ValueTable)": enum_table,
            "Initial Value": sig.initial,
            "Comment": sig.comment
        })

df = pd.DataFrame(rows)
df.to_csv("./p_data/signals_summary_v2.csv", index=False, encoding="utf-8-sig", quoting=csv.QUOTE_NONNUMERIC)  # Để Excel mở không lỗi font