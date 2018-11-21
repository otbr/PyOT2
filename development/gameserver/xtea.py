# as small and simple pure-Python ECB XTEA encrypion/decryption algorithms as possible

def Encrypt():
	key = bytes.fromhex("b79cbed936812e6b195095fa61da107e")
	data = bytes.fromhex("64010500537661727407005265616c6f74737f000001041c3905000000000000")
	# actual encryption here...

	print(data.hex()) # ee8971009b948ec20192d7f8d873a994c2c03f7bcc22bfc38d7a35962e1e76bb


def Decrypt():
	key = bytes.fromhex("b79cbed936812e6b195095fa61da107e")
	data = bytes.fromhex("ee8971009b948ec20192d7f8d873a994c2c03f7bcc22bfc38d7a35962e1e76bb")
	# actual decryption here...

	print(data.hex()) # 64010500537661727407005265616c6f74737f000001041c3905000000000000")
