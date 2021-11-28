class Selectorss:

    xpath_input_login = '//input[@name="UserName"]'
    xpath_input_password = '//input[@name="Password"]'
    xpath_button_autorization = '//button[@id="logonBtn"]'

    ############################################################################################
    # Для страницы "Заявки на пропуска / Временный пропуск"

    xpath_vrem_propusk = '//div/a[@title="Оформление заявки на временный пропуск"]'

    xpath_last_name = '//div/input[@id="Visitor_LastName"]'
    xpath_first_name = '//div/input[@id="Visitor_Firstname"]'
    xpath_middle_name = '//div/input[@id="Visitor_MiddleName"]'

    xpath_down_link ='//ul[@aria-activedescendant="ui-active-menuitem")]'
    xpath_firm_value = '/html/body/div[1]/div[3]/div[1]/div[2]/div/div/form/div/div[1]/div[1]/div[1]/fieldset[1]/div/div/div/div/div[4]/div/div[2]/input'

    xpath_birthday = '//input[@id="Visitor_Birthdate"]'
    xpath_foreign_person_chekbox = '//input[@id="Visitor_IsAlienBool"]'

    xpath_visitor_email = '//input[@id="Visitor_Email"]'

    xpath_code_country_drop_down_list = '//select[@id="prefix"]'
    xpath_number_mobile_phone = '/html/body/div[1]/div[3]/div[1]/div[2]/div/div/form/div/div[1]/div[1]/div[1]/fieldset[1]/div/div/div/div/div[8]/div[2]/div/div[2]/input'

    xpath_beginning_validity_period = '//input[@id="RequestInterval_FromDate"]'
    xpath_expiration_validity_period = '//input[@id="RequestInterval_ToDate"]'

    xpath_purpose_visit = '//div/input[@id="Objective_Value"]'

    xpath_input_file = '//input[@type="file"]'

    xpath_FIO_host_party = '//input[@id="Host_Person_Value"]'
    xpath_FIO_number_in_list_host_party = '//ul/li/a[@tabindex="-1"]'
    # '/html/body/ul[12]/li[1]/a'
    # '/html/body/ul[13]/li[2]/a'


    xpath_host_party_address = '//input[@id="Host_Place_Value"]'
    xpath_number_in_list_host_party_address = '/html/body/ul[14]/li[1]/a/div'
    # '/html/body/ul[15]/li[1]/a/div'

    xpath_host_room = '//input[@id="Host_Room"]'
    xpath_host_phone = '//input[@id="Host_Phone"]'

    xpath_users_document = '//div/a[contains(text(),"Документ посетителя")]'
    xpath_document_type = '//select[@id="VisitorDocumentModel_SelectedVisitorDocument"]'
    xpath_document_series = '//input[@id="VisitorDocumentModel_VisitorDocument_Seria"]'

    xpath_document_number = '/html/body/div[1]/div[3]/div[1]/div[2]/div/div/form/div/div[1]/div[1]/div[2]/fieldset/div/div/div[2]/div/div[2]/input'
    xpath_document_authority = '//input[@id="VisitorDocumentModel_VisitorDocument_Athority"]'
    xpath_document_code = '//input[@id="VisitorDocumentModel_VisitorDocument_Code"]'
    xpath_document_date = '//input[@id="VisitorDocumentModel_VisitorDocument_ReleaseDate"]'
    xpath_place_of_registration = '//input[@id="VisitorDocumentModel_VisitorDocument_Misc"]'

    xpath_wealth = '//div/a[contains(text(),"Материальные ценности")]'
    xpath_checkbox_move_in = '//input[@id="MoveIn"]'
    xpath_checkbox_move_out = '//input[@id="MoveOut"]'
    xpath_document_of_wealth = '//input[@id="DeviceModel_Device_Name"]'
    xpath_wealth_model = '//input[@id="DeviceModel_Device_Model"]'
    xpath_wealth_serial_number = '//input[@id="DeviceModel_Device_SerialNumber"]'
    xpath_wealth_count = '//input[@id="DeviceModel_Device_DeviceVisitorRequest_Count"]'
    xpath_wealth_unit = '//input[@id="DeviceModel_Device_DeviceVisitorRequest_Units"]'
    xpath_wealt_unit_number = '/html/body/ul[16]/li[2]/a'
    xpath_wealth_add = '//button[@id="btnAddModel"]'

    xpath_car = '//div/a[contains(text(),"Автомобиль")]'
    xpath_car_number = '//input[@id="VisitorCarModel_VisitorCar_Car"]'
    xpath_car_brand = '//input[@id="VisitorCarModel_VisitorCar_CarMark"]'
    xpath_car_brand_in_list = '/html/body/ul[9]/li/a/div'
    xpath_car_color = '//input[@id="VisitorCarModel_VisitorCar_CarColor"]'
    xpath_checkbox_night_car = '//input[@id="VisitorCarModel_StayCar"]'
    xpath_checkbox_permission_unload_car = '//input[@id="VisitorCarModel_CarUnloading"]'


    xpath_button_save = '//button[@id="saveBtn"]'
    xpath_parking_place = '//input[@id="VisitorCarModel_ParkingPlaceName"]'
    xpath_parking_place_in_list = '/html/body/ul[8]/li/a/div'

    ############################################################################################
    # Для страницы "Заявки на пропуска / Разовый пропуск "
    xpath_raz_propusk_RP = '//div/a[@title="Оформление заявки на разовый пропуск"]'

    xpath_last_name_RP = '//div/input[@id="Visitor_LastName"]'
    xpath_first_name_RP = '//div/input[@id="Visitor_Firstname"]'
    xpath_middle_name_RP = '//div/input[@id="Visitor_MiddleName"]'

    xpath_beginning_validity_period_RP = '//input[@id="RequestInterval_FromDate"]'
    xpath_expiration_validity_period_RP = '//input[@id="RequestInterval_ToDate"]'

    xpath_count_RP = '//div/input[@id="Request_NumOfVisits"]'

    xpath_FIO_host_party_RP = '//input[@id="Host_Person_Value"]'
    xpath_FIO_number_in_list_host_party_RP = '//ul/li/a[@tabindex="-1"]'

    xpath_host_party_address_RP = '//input[@id="Host_Place_Value"]'
    xpath_number_in_list_host_party_address_RP = '/html/body/ul[14]/li[1]/a/div'

    xpath_again_create_RP = '//button[@id="btnNew"]'

    ############################################################################################
    # Для страницы "Групповой пропуск"
    xpath_group_propusk = '//div/a[@title="Оформление заявки на групповое посещение"]'

    xpath_FIO_group_host_party = '//input[@id="Host_Person_ID"]'
    # '//input[@id="Host_Person_Value"]'
    xpath_FIO_group_host_party_2 = '//ul/li/a[@tabindex="-1"]'
    xpath_FIO_group_host_party_list = '/html/body/ul[12]/li[1]/a'
    # '/html/body/ul[12]/li[1]/a'
    # '/html/body/ul[12]/li[1]/a

    xpath_group_address_host_party = '//input[@id="Host_Place_Value"]'
    xpath_group_address_host_party_list = '/html/body/ul[14]/li/a/div'
    # '/html/body/ul[14]/li[5]/a/div'

    #'/html/body/ul[14]/li[8]/a/div'
    # '/html/body/ul[14]/li[8]/a/div'
    # '//ul/li/a[@tabindex="-1"]'
    # '/html/body/ul[14]/li[1]/a/div'
    # '//ul/li/a[@tabindex="-1"]'
    # '/html/body/ul[12]/li[1]/a'

    xpath_button_add_visitor = '//button[@id="btnAddVisitor"]'

    ############################################################################################
    # Для страницы "Материальный пропуск"
    xpath_material_propusk = '//div/a[@title="Оформление заявки на материальный пропуск"]'

    xpath_date_material_propusk = '//input[@id="Request_DateFrom"]'

    xpath_material_propusk_check_box_vnos = '//*[@id="Addition_DirectionIn"]'
    xpath_material_propusk_chek_box_vynos = '//*[@id="Addition_DirectionOut"]'

    xpath_wealth_unit_number_in_list = '/html/body/ul[11]/li[2]/a'


    ############################################################################################
    # Для страницы "Оформление пропуска по предварительной заявке"

    xpath_passes = '//span[text()="Пропуска"]'

    xpath_raz_propusk_by_request = '//div/a[@title="Оформление пропуска по заявке"]'

    xpath_last_name_in_reguest = '//*[@id="VisitorModel_Visitor_LastName"]'
    xpath_first_name_in_reguest = '//*[@id="VisitorModel_Visitor_Firstname"]'
    xpath_middle_name_in_reguest = '//*[@id="VisitorModel_Visitor_MiddleName"]'

    xpath_fio_in_list_request = '/html/body/ul[2]/li/a/div[1]'

    xpath_free_card_list = '//button[@id="cardListBtn"]'

    xpath_first_free_card = '//td[text()="001002B38EE3"]'
    xpath_select_first_free_card = '//button[text()="Выбрать"]'


    xpath_save_RP = '//button[@id="btSend"]'

    xpath_close_window_RP = '//span[text()="close"]'

    xpath_all_pass = '//span[@id="VisitsStatus"]'

    xpath_this_pass = '//td[text()="1секретарь2 Секретарь2 1"]'

    xpath_in_system_go = '//button[@cls = " dialog-ok-button btn-flat waves-effect hilight"]'

    xpath_pass_delivery_button = '//button[@data-direction="Exit"]'
    xpath_ok_button_mark_made = '//button[text()="OK"]'
    # -----------------------------------------------------------
    xpath_test_link1 = '//a[text()="A/B Testing"]'
    # ------------------------------------------------------------
    #  Для тестового задания от компании "Tenzor"
    xpath_yandex_search = '//input[@id="text"]'
    xpath_yandex_suggest = '//ul[@class="mini-suggest__popup-content"]'
    xpath_elements = '//span[@class="OrganicTitleContentSpan"]/b'
    xpath_elements2 = '//div[@class="Path Organic-Path path organic__path"]/a'
    xpath_yandex_image_link = '//a[@data-id="images"]'
    xpath_yandex_search_image_string = 'div[@class="search2__input"]'
    xpath_yandex_search_image1 = 'span[@class="input__box"]'
    xpath_yandex_search_image2 = 'span[@class="input__box"]/input'
    xpath_yandex_search_image3 = 'span[text()="Будьте в Плюсе"]'
    xpath_yandex_search_image4 = 'input[@id="uniq1637920368676188993"]'
    xpath_yandex_search_image5 = '/html/body/header/div/div[2]/div[1]/form/div[1]/span/span/input'

    xpath_yandex_image1_pumpkin = '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a'
    xpath_yandex_image2_pumpkin = '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a'

    xpath_next_image_button ='/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]/i'
    xpath_prev_image_button ='/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/i'

    xpath_prev_image = '/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img'










