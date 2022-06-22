

def main():
    user_input = input("""What is the Answer to the Great Question of Life, the Universe, and Everything? """).lower()
    valid_input = ['42', 'forty-two', 'forty two']
    if user_input in valid_input:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
