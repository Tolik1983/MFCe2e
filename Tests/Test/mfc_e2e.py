from Tests.mfc_testing.model import mfc


def test_mfce2e():
    mfc.open()
    mfc.search('сироватка')
    mfc.open_item_page()
    #cart
    mfc.button_add_to_cart_click()
    mfc.cart_click()
    mfc.cart_icon_plus()
    mfc.cart_icon_minus()
    mfc.cart_close_click()
    #authorization
    mfc.profile_icon_click()
    mfc.login_data_input('olga.mochaieva@gmail.com', 'olyaolya')
    #personal data change
    mfc.personal_data_click()
    mfc.account_name_change('Тетяна')
    mfc.account_name_change('Ольга')
    mfc.logout()

    #negative tests
    mfc.profile_icon_click()
    mfc.login_data_input('olga.mochaieva', 'olyaolya')
    mfc.negative_login()
    mfc.login_data_input('olga.mochaieva@gmail.com', 'tanya')
    mfc.negative_password()


