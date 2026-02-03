from menu import get_auth_menu,get_print_menu


get_print_menu()

def run():
    while True:
        get_auth_menu()
        choise = input("Variantni tanlang: ")
        
        if choise == "1":
            # login_comman
            pass
        elif choise == "2":
            # register_command()
            pass
        
        elif choise == "0":
            print("Xayr siz dasturdan chiqdingiz! ")
            exit(0)
            
        else:
            print("Noto'g'ri variant. Qaytadan urinib ko'ring.")
            
            
if __name__ == "__main__":
    run()
    
    