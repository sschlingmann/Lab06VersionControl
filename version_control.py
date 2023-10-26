# This function takes in a number in string format and encodes it to increase each digit by 3.
# Programmed by Scott Schlingmann
def encode(orig_num):
    encoded_num = ''
    for i in range(len(orig_num)):
        digit = str((int(orig_num[i]) + 3) % 10)
        encoded_num += digit
    return encoded_num

def decode(encoded_num):  # Takes in integer password as a string and decodes it back to original string. -Scott
    result = ''
    for i in encoded_num:
        result += str((int(i)+7) % 10)
    return result


# Now we will define the main function.
def main():
    option = None
    while option != 3:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            orig_num = input('Please enter your password to encode: ')
            encoded_num = encode(orig_num)
            print('Your password has been encoded and stored!\n')


        if option == 2:
            print(f"The encoded password is {encoded_num}, and the original password is {decode(encoded_num)}.")


if __name__ == '__main__':
    main()
    
