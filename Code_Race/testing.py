test_cases = [
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00000000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Tất cả tín hiệu đều OFF
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00001000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Brake fluid ON (bit 3)
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00010000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # VSA OFF ON (bit 4)
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00000100, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Door open ON (bit 2)
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00011100, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Cả 3 tín hiệu ON
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00011000, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Brake fluid + VSA ON
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00010100, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Door + VSA ON
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00001100, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],  # Door + Brake ON
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b11111111, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],  # All bits ON (test overload)
    },
    {
        'arbitration_id': 0x1A6,
        'dlc': 8,
        'data': [0b00000010, 0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE],  # Random data, bit 1 ON
    },
]

from decode_signals import gen_signal

def run_tests():
    for i, test_case in enumerate(test_cases):
        CAN_Frame = test_case.copy()
        print(f"\n---------------- Running test case {i + 1}: {test_case} ----------------\n")
        CAN_Frame['arbitration_id'] = test_case['arbitration_id']
        CAN_Frame['dlc'] = test_case['dlc']
        CAN_Frame['data'] = test_case['data']
        gen_signal(CAN_Frame)
        print("\n--------------------------------------------------\n")
        # Call the decoding function or any other relevant function here

if __name__ == "__main__":
    run_tests()