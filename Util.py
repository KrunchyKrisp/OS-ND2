disk_path = 'hdd.txt'
word_length = 4
block_length = 16
vm_blocks = 16
page_blocks = 1
ram_blocks = 64
user_blocks = 44
shared_blocks = 4
system_blocks = 16
total_bytes = ram_blocks * block_length * word_length


def int_to_hex(value: int) -> [bytes]:
    data = value.to_bytes(4, 'big')
    return [data[i:i + 1] for i in range(len(data))]


def hex_to_int(value: [bytes]) -> int:
    return int.from_bytes(b''.join(value), 'big')
