from selenium.webdriver.common.by import By

class MainPageLocators:
    constructor_btn = (By.XPATH, ".//ul[@class = 'AppHeader_header__list__3oKJj']//p[text() = 'Конструктор']")  # Кнопка конструктор
    order_feed_btn =  (By.XPATH, ".//ul[@class = 'AppHeader_header__list__3oKJj']//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    popup_window = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']") #Всплывающее окно  
    cross_btn = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") #Крестик закрывающий всплывающее окно
    first_ingredient = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']/parent::a") #Первый ингредиент
    counter_main_page = (By.XPATH, ".//div[@class='counter_counter__ZNLkj counter_default__28sqi']") #Счетчик количества ингредиентов в заказе
    order_panel = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']") #Панель заказа
    set_order_btn = (By.XPATH, ".//button[text()='Оформить заказ']") #Кнопка оформить заказ
    heading_main_gape = (By.XPATH, ".//section/h1[text()='Соберите бургер']") #Заголовок Соберите бургер на главной странице
    heading_order_feed = (By.XPATH, ".//h1[text()='Лента заказов']") #Заголовок Лента заказов на странице ленты заказов
    #Количество выполненных заказов за время время
    total_orders = (By.XPATH, ".//div[contains(@class, 'mb-15')]//p[text()='Выполнено за все время:']/following-sibling::p")
    #Количество выполненных заказов за сегодня
    today_orders = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    #список заказов в работе
    order_list_ready = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]")
    # Конкретный заказ в списке
    order_items = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text_type_digits-default')]")
    personal_account_btn = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']")
    registrate_footer_btn = (By.XPATH, ".//a[text()='Зарегистрироваться']") #Кнопка зарегистрироваться
    register_title = (By.XPATH, ".//h2[text()='Регистрация']") #Заголовок экрана регистрации
    name_input = (By.XPATH, ".//input[@name='name' and @type='text']") #Поле ввода имени при регистрации
    email_input = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']") #Поле ввода email при регистрации
    password_input = (By.XPATH, ".//input[@type='password' and @name='Пароль']") #Поле ввода пароля при региcтрации
    register_btn = (By.XPATH, ".//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']") #Кнопка зарегистрироваться под полями ввода
    email_field_auth = (By.XPATH, ".//label[text()='Email']/following-sibling::input") #Поле ввода email при авторизации
    password_field_auth = (By.XPATH, ".//input[@type='password' and @name='Пароль']") #Поле ввода пароля при авторизации
    login_title_auth = (By.XPATH, ".//h2[text()='Вход']") #Заголовок при авторизации
    login_auth_btn = (By.XPATH, ".//button[text()='Войти']") #Кнопка Войти при авторизации
    button_auth = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") #кнопка войти в аккаунт

