from selenium.webdriver.common.by import By


class LocatorsPageCreateCourse:
    APPEARANCE_DATA = (By.XPATH, "//a[text()='Внешний вид']")
    COURSE_DESCRIPTION = (By.ID, "id_summary_editoreditable")
    COURSE_FORMAT_DATA = (By.XPATH, "//a[text()='Формат курса']")
    COURSE_LANGUAGE = (By.ID, "id_lang")
    CREATE_COURSE_HEADER = (By.TAG_NAME, "h2")
    END_DAY = (By.ID, "id_enddate_day")
    END_HOUR = (By.ID, "id_enddate_hour")
    END_MINUTE = (By.ID, "id_enddate_minute")
    END_MONTH = (By.ID, "id_enddate_month")
    END_YEAR = (By.ID, "id_enddate_year")
    FILE_DATA = (By.XPATH, "//a[text()='Файлы и загрузки']")
    FULL_COURSE_NAME = (By.ID, "id_fullname")
    GENERAL_DATA = (By.ID, "id_general")
    MANAGER_NAME = (By.ID, "id_role_1")
    MAX_FILE_SIZE = (By.ID, "id_maxbytes")
    NEW_COURSE_HEADER = (By.CLASS_NAME, "page-header-headings")
    ROLE_RENAME_DATA = (By.XPATH, "//a[text()='Переименование ролей']")
    SAVE_AND_SHOW_BUTTON = (By.ID, "id_saveanddisplay")
    SECTION_NUMBER = (By.ID, "id_numsections")
    SHORT_COURSE_NAME = (By.ID, "id_shortname")
    STUDENT_NAME = (By.ID, "id_role_5")
    TEACHER_NAME = (By.ID, "id_role_3")