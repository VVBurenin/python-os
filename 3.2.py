def user_data (name, surename = 'guest', brdate = '01.01.2000', city = 'Default city', email = 'exz@exz.com', tel = 00):
    return(f'{name} {surename} {brdate} год(а) рождения, проживает в городе {city}, контактная информация:'
           f'телефон {tel}, e-mail - {email}')


petr_info = user_data(name='Petr', surename='Kuzmin', brdate='11.11.2000', city='Moskow', email='petro2020@gmail.com',
                      tel=89165544777)
print(petr_info)
