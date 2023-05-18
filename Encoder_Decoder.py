import tkinter as tk


def encode_rle(data):

    # Encode a string or list using Run Length Encoding (RLE).

    encoded = []
    i = 0
    while i < len(data):
        count = 1
        while i + count < len(data) and data[i] == data[i + count]:
            count += 1
        if count > 1:
            encoded.append(str(count))
        encoded.append(data[i])
        i += count
    return ''.join(encoded)

def decode_rle(encoded_data):

    # Decode a string that has been encoded using Run Length Encoding (RLE).

    decoded = []
    i = 0
    while i < len(encoded_data):
        if encoded_data[i].isdigit():
            count = int(encoded_data[i])
            decoded.append(encoded_data[i+1] * count)
            i += 2
        else:
            decoded.append(encoded_data[i])
            i += 1
    return ''.join(decoded)




def encode_callback():

    # Callback function for the Encode button.
        
    data = input_text.get('1.0', 'end-1c')
    encoded_data = encode_rle(data)
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', encoded_data)

def decode_callback():
    
    # Callback function for the Decode button.
    
    encoded_data = input_text.get('1.0', 'end-1c')
    decoded_data = decode_rle(encoded_data)
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', decoded_data)

# Create the main window
root = tk.Tk()
root.title('RLE Encoder/Decoder')

# Create the input and output text widgets
input_text = tk.Text(root, height=10, width=50)
input_text.pack(side=tk.LEFT, padx=10, pady=10)
output_text = tk.Text(root, height=10, width=50)
output_text.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the Encode and Decode buttons
encode_button = tk.Button(root, text='Encode', command=encode_callback)
encode_button.pack(side=tk.TOP, padx=10)
decode_button = tk.Button(root, text='Decode', command=decode_callback)
decode_button.pack(side=tk.BOTTOM, padx=10)

# Start the main event loop
root.mainloop()


# data = 'AAABBBCCCCDDDEEEE'
# encoded_data = encode_rle(data)
# print(encoded_data)  # prints '3A3B4C3D4E'
# decoded_data = decode_rle(encoded_data)
# print(decoded_data)  # prints 'AAABBBCCCCDDDEEEE'