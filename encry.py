import base64



c=input("")

ciphertext = []






def enc_msg(message):
    for char in message:
        encrypted_char = (123 *ord(char) + 18) % 256
        ciphertext.append(encrypted_char)
        ret = bytes(ciphertext)# Base64 encoder
    return ret


print(enc_msg(c))

print(bytes("77"))

# print(enc_msg(c))
# def encrypt_message(message):
#     ciphertext = []

#     # Iterate through each character in the input message
#     for char in message:
#         # Encrypt each character using a simple algorithm
#         encrypted_char = (123 * ord(char) + 18) % 256
#         # Append the encrypted value to the ciphertext list
#         ciphertext.append(encrypted_char)
#         encrypted_bytes = bytes(ciphertext)

#     # Convert the list of encrypted values to bytes
   

#     # Perform Base64 encoding on the encrypted bytes
#     #encoded_result = base64.b64encode(encrypted_bytes)

#     # Return the Base64-encoded result
#     return encrypted_bytes

# # Example usage
# message_to_encrypt = "kngaon"
# encrypted_result = encrypt_message(message_to_encrypt)
# for i in encrypted_result:
#     print("Encrypted Result:", (i))


