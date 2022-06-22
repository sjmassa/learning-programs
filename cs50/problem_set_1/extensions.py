

def main():
    user_input = input("File name: ").lower().strip()
    if '.jpg' in user_input or '.jpeg' in user_input:
        print('image/jpeg')
    elif '.gif' in user_input:
        print('image/gif')
    elif '.png' in user_input:
        print('image/png')
    elif '.pdf' in user_input:
        print('application/pdf')
    elif '.txt' in user_input:
        print('text/plain')
    elif '.zip' in user_input:
        print('application/zip')
    else:
        print("application/octet-stream")

if __name__ == '__main__':
    main()
