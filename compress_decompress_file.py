import zlib, base64

#compressing file
data = open('file.txt', 'r').read()
data_bytes = bytes(data, 'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes))
decoded_data = compressed_data.decode('utf-8')
compressed_file = open('compressed.txt','w')
compressed_file.write(decoded_data)


#decompressing file
decompressed_data = zlib.decompress(base64.b64decode(compressed_data))

