from termcolor import colored,cprint

class AuthCommands:
    
    def Login(self)->None:
        
        text = colored("Dasturga kirish uchun login va password kiriting","blue")
        cprint(text)
        
        username = input("Username kiriting: ").strip()
        password = input("Passwordni kiriting: ").strip()
        
    def Register(self)-> None:
        
        text = colored("Registratsiya qilish uchun quyidagilarni tuldiring","blue")
        cprint(text)
        cprint(colored("~" * 40,"blue"))
        
        last_name = input("Familiyangizni kiriting: ").strip()
        first_name = input("Ismingizni kiriting: ").strip()
        username = input("Username kiriting: ").strip()
        password = input("Passwordni kiriting: ").strip()
        