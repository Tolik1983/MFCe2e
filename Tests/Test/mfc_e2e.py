from time import sleep
from selene.support.shared.jquery_style import s, ss
from Tests.mfc_testing.model import port


def test_mfce2e():
    port.open()
    port.search('сироватка')
    port.open_item_page()
    sleep(3)
    port.button_add_to_cart_click()
    sleep(1)
    port.cart_click()
    sleep(1)
    port.cart_icon_plus()
    sleep(1)
    port.cart_icon_minus()
    sleep(1)
    port.cart_close_click()
    port.profile_icon_click()
    port.login_data_input('olga.mochaieva@gmail.com', 'angedonia91')
    sleep(3)
    port.personal_data_click()
    sleep(2)
    port.account_name_change('Тетяна')
    sleep(2)
    port.account_name_change('Ольга')
    port.logout()
    #negative tests
    port.profile_icon_click()
    port.login_data_input('olga.mochaieva', 'angedonia91')
    port.negative_login()
    port.login_data_input('olga.mochaieva@gmail.com', 'angedonia')
    port.negative_password()
    sleep(3)

