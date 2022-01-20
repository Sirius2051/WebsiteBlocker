import os

class WebsiteBlocker:
    def __init__(self):
        self.os_name = os.name
        self.websites = []
        self.route = ""

    def Main(self):
        self.Route()
        self.InputControl()
        self.Blocker()
        if len(self.websites) > 0:
            print('\033[;32mOperations successfully completed.')
        else:
            print('\033[;31m'+'You have not indicated any website.')

    def InputControl(self):
        text = input('\033[;35m\t')
        if text == 'ok':
            pass
        else:
            self.websites.append(text)
            self.InputControl() 

    def Blocker(self):
        with open(self.route, 'r+') as file:
            content = file.read()
            for website in self.websites:
                if website in content:
                    pass
                else:
                    line = f'127.0.0.1 \t { website } \n'
                    file.write(line)

    def Route(self):
        if self.os_name == 'posix':
            self.route = '/etc/hosts'
        elif self.os_name == 'nt':
            self.route = 'C:\Windows\System32\drivers\etc\hosts'
        else:
            print('\033[;31mYour operating system is not supported. Please contact us.')

print("""
\033[1;33m
----------------------------------------------------------------
\033[1;32m
       __          __  _         _ _       
       \ \        / / | |       (_) |      
        \ \  /\  / /__| |__  ___ _| |_ ___ 
         \ \/  \/ / _ \ '_ \/ __| | __/ _ \\
          \  /\  /  __/ |_) \__ \ | ||  __/
           \/  \/ \___|_.__/|___/_|\__\___|
                                           
                                           
         ____  _            _             
        |  _ \| |          | |            
        | |_) | | ___   ___| | _____ _ __ 
        |  _ <| |/ _ \ / __| |/ / _ \ '__|
        | |_) | | (_) | (__|   <  __/ |   
        |____/|_|\___/ \___|_|\_\___|_|          
\033[1;33m
----------------------------------------------------------------
\033[;33mEnter a URL or write \'ok\' to close the program.
""")

website_blocker = WebsiteBlocker()
website_blocker.Main()