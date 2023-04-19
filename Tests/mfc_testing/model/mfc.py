from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have
from selene.support.conditions import be



class Mfc:
    def __init__(self):
        self.base_url = 'https://mariefreshcosmetics.com/'


    def open(self):
        browser.open('https://mariefreshcosmetics.com/')
        browser.driver.maximize_window()
        return self


    def search(self, port: str):
        browser.element('[placeholder="Пошук"]').type(port).press_enter()
        return self


    def open_item_page(self):
        browser.element('[href="/products/serum"]').click()
        return self


    def button_add_to_cart_click(self):
        browser.element('[href="/item?variant_id=225"]').click()
        return self


    def cart_click(self):
        s('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/div[2]/a[1]/span[2]').click()
        return self



    def cart_icon_plus(self):
        s('.icon-plus').click()
        return self


    def cart_icon_minus(self):
        s('.icon-minus').click().click()
        return self

    def cart_close_click(self):
        s('[title="Close"]').click()
        return self

    def profile_icon_click(self):
        ss('.action_link_title')[2].click()
        return self

    def login_data_input(self, login_name: str, login_pass: str):
        s('#account_email').click().clear().type(login_name)
        s('#account_password').click().clear().type(login_pass)
        s('[type="submit"]').click()
        return self

    def personal_data_click(self):
        s('[href="/account/profile"]').click()
        return self


    def account_name_change(self, test_name: str):
        s('#account_name').click().clear().type(test_name)
        s('.button').click()
        s('#account_name').should(have.value(test_name))

    def logout(self):
        s('[href="/auth/logout"]').click()
        return self

    def negative_login(self):
        s('#account_email-error').should(be.visible)
        return self

    def negative_password(self):
        s('.validation_error').should(be.visible)
        return self