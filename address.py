from cryptography.fernet import Fernet


bridge_ip_address = "192.168.1.11"


key = Fernet.generate_key()

fernet = Fernet(key)
 
encbridge_ip_address = fernet.encrypt(bridge_ip_address.encode())

# print("original string: ", bridge_ip_address)
print("bridge_ip_address: ", encbridge_ip_address)


'''
- to print original string :

decbridge_ip_address = fernet.decrypt(encbridge_ip_address).decode()
print("bridge_ip_address: ", decbridge_ip_address)

'''