import datetime

class Selectorss:
   
    xpath_input_login = '//input[@name="UserName"]'
    xpath_input_password = '//input[@name="Password"]'
    xpath_button_autorization = '//button[@id="logonBtn"]'

    ############################################################################################
    # Для страницы "Временный пропуск"

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
    xpath_FIO_number_in_list_host_party = '/html/body/ul[13]/li[2]/a'
   

    xpath_host_party_address = '//input[@id="Host_Place_Value"]'
    xpath_number_in_list_host_party_address = '/html/body/ul[15]/li[1]/a/div'

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
    # Для страницы "Разовый пропуск "
    xpath_raz_propusk = '//div/a[@title="Оформление заявки на разовый пропуск"]'

    ############################################################################################
    # Для страницы "Групповой пропуск"
    xpath_group_propusk = '//div/a[@title="Оформление заявки на групповое посещение"]'

    xpath_FIO_group_host_party = '//input[@id="Host_Person_Value"]'
    xpath_FIO_group_host_party_list = '/html/body/ul[12]/li[2]/a'

    xpath_button_add_visitor = '//button[@id="btnAddVisitor"]'

    xpath_group_address_host_party = '//input[@id="Host_Place_Value"]'
    xpath_group_address_host_party_list = '/html/body/ul[14]/li/a/div'

    ############################################################################################
    # Для страницы "Материальный пропуск"
    xpath_material_propusk = '//div/a[@title="Оформление заявки на материальный пропуск"]'

    xpath_date_material_propusk = '//input[@id="Request_DateFrom"]'

    xpath_material_propusk_check_box_vnos = '//*[@id="Addition_DirectionIn"]'
    xpath_material_propusk_chek_box_vynos = '//*[@id="Addition_DirectionOut"]'

    xpath_wealth_unit_number_in_list = '/html/body/ul[11]/li[2]/a'

    

    
    
    
 
   