def send_email(message, recipient, sender = 'university.help@gmail.com'):
     if sender == recipient:
          print('Невозможно отправить письмо самому себе')
          return

     if '@' in recipient and recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4:] == ".net":
           if '@' in sender and sender[-4:] == '.com' or sender[-3:] == '.ru' or sender[-4:] == ".net":
               if sender != 'university.help@gmail.com':
                    print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
               if sender == 'university.help@gmail.com':
                    print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
                    return
     else:
          print('Невозможно отправить письма с адреса', sender, 'на адрес', recipient)
          return




send_email('Команда <break> используется только в циклах', 'Vasia. pamiati@.net')
send_email('Не забывай кавычки!', 'Vasia. pamiati@.net', sender = 'urban@mail.ru')
send_email('Бе-бе-бе', 'Vasia. pamiati@.ne')
send_email('Se hace camino al andar', 'Vasia. pamiati@.net', sender = 'Vasia. pamiati@.net')
send_email('Caminante, no hay camino', 'Vasia. pamiati@.net', sender = 'Vasia.ty@gde')




