def hello_command(args, contacts):
    return 'How can I help you?'

def add_contact(args, contacts):
    if len(args) != 2:
        return 'Incorrect number of arguments. Please provide both name and phone number.'
    
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    if len(args) != 2:
        return 'Incorrect number of arguments. Please provide both name and phone number.'
    
    name, phone = args
    if name and name in contacts.keys():
        contacts[name] = phone
        return 'Contact updated.'

def show_phone(args, contacts):
    if len(args) != 1:
        return 'Please provide both name of the contact.'
    
    name = args
    if name:
        return contacts.get(name[0], 'Contact not found')
    return 'You need to point out username, please!'

def show_all(args, contacts):
    return contacts

def exit_command(args, contacts):
    return 'Good bye!'

def list_commands(args, contacts):
    command_list = '\n'.join(f'{cmd.__name__}: {", ".join(words)}' for cmd, words in COMMAND_HANDLER.items())
    return f'Available commands:\n{command_list}'

def unknown_command(args, contacts):
    return 'Unknown command. Use "list" to see all available commands.'

COMMAND_HANDLER = {
    hello_command: ['hello', 'hi', 'привіт'],
    add_contact: ['add', 'додати'],
    change_contact: ['change', 'змінити'],
    show_phone: ['phone', 'number', 'телефон', 'номер'],
    show_all: ['all', 'усі'],
    exit_command: ['exit', 'close', 'quit', 'q', 'вийти'],
    list_commands: ['list', 'команди']
}

def parser(user_input: str):
    for cmd, words in COMMAND_HANDLER.items():
        for word in words:
            if user_input.startswith(word):
                return cmd, user_input[len(word):].split()
    return unknown_command, []

def main():
    print('Welcome to phone assistant bot!')
    contacts = {}
    while True:
        user_input = input('Enter a command: ')
        cmd, data = parser(user_input)
        print(cmd(data, contacts))
        if cmd == exit_command:
            break

if __name__ == '__main__':
    main()