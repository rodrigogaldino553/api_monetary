import requests, time


def lines(how_much):
    print('='*how_much)
    
    
def get_info(code):
    url = 'https://economia.awesomeapi.com.br/all/'+code

    return requests.get(url).json()



def show_infos(coin, coin_name):
    lines(36)
    print('{:^36}'.format('Data about '+coin_name))
    lines(36)
    
    for k, v in coin[coin_name].items():
        print('{:.<15}{}'.format(k, v))
    

while True:
    
    print('Example: USD-BRL to see dollar to real')
    coin_code = str(input('Type coin code: ')).strip().upper()

    show_infos(get_info(coin_code), coin_code)
   
    lines(36)
    
    print('Do you want see others[Y/N]')
    cont = str(input(' : ')).strip().upper()
    
    if 'N' in cont:
        print('Come back always!')
        break
