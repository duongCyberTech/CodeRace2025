import pandas as pd

pfile = './p_data/signals_summary_v2.csv'
efile = './p_data/error_signals_summary.csv'

dfp = pd.read_csv(pfile, encoding="utf-8-sig")
dfe = pd.read_csv(efile, encoding="utf-8-sig")

def decode_signal(signal, can_frame):
    start_bit = signal['StartBit']
    length = signal['Length']
    is_little_endian = signal['Endianess'] == 'little_endian'
    is_signed = signal.get('Signed', False)
    factor = signal.get('Factor', 1.0)
    offset = signal.get('Offset', 0.0)

    # Chuyển frame thành số nguyên 64 bit
    raw_int = int.from_bytes(can_frame, byteorder='little' if is_little_endian else 'big')

    # Dịch để lấy đúng đoạn bit
    if is_little_endian:
        bit_pos = start_bit
    else:
        byte_index = start_bit // 8
        bit_in_byte = start_bit % 8
        bit_pos = (7 - byte_index) * 8 + bit_in_byte - length + 1

    mask = (1 << length) - 1
    value = (raw_int >> bit_pos) & mask

    # Xử lý giá trị signed (Có dấu)
    if is_signed and (value & (1 << (length - 1))):
        value -= (1 << length)

    # Áp dụng scale, offset
    return value * factor + offset

def gen_signal(CAN_Frame):
    df_signals = dfp.loc[dfp['ID'] == hex(CAN_Frame['arbitration_id'])]
    print(f"Decoded signals for CAN Frame ID {hex(CAN_Frame['arbitration_id'])}:")
    for _, signal in df_signals.iterrows():
        value = decode_signal(signal, CAN_Frame['data'])
        print(f" - {signal['Signal']}: {value}")

