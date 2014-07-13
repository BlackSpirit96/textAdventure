def print_text(text):
	print '-' * 10
	print text
	print '-' * 10

def main(cheatmone = False):
	message = """
You wake up in a small room with a bed and a book on a desk.
There is also a door and a window that you can see outside.
what will you do ?
"""
	print_text(message)
	action = raw_input("> ")

if __name__ == "__main__":
    main()