from guizero import App, Text, TextBox, Slider, Combo, ButtonGroup, Box, PushButton, info

window = App(title = "Thẻ hội viên CLB Thể thao")

# Function to register
def check_email(to_check_email):
    global email
    to_check_email = email.value.strip()
    if " " in to_check_email:
        return False
    if "@" not in to_check_email:
        return False
    return True
def register():
    global name
    global school
    global height
    global email
    global phone_num
    global gender

    reg_name = name.value.strip()
    reg_school = school.value.strip()
    reg_height = height.value
    reg_email = email.value.strip()
    reg_phone_num = phone_num.value
    reg_gender = gender.value.strip()
    
    #if reg_name.isalpha() == False:
     #   info(title = "Notification", text = "Tên không thể có số")
    if check_email(reg_email) == False:
        info(title = "Notification", text = "Email không hợp lệ!")
    elif reg_phone_num.isdigit() == False:
        info(title = "Notification", text = "Số điện thoại chỉ được có kí tự số!")
    elif reg_name == "" or reg_email == "" or reg_phone_num == "":
        info(title = "Notification", text = "Các phần thông tin không được để trống")
    else:
        with open("storage.txt", "a", encoding = "utf-8") as f:
            f.write(f"{reg_name} | {reg_school} | {reg_height} | {reg_email} | {reg_phone_num} | {reg_gender} \n")
    
        
    
# GUI Part
box_of_wisdom = Box(window, layout = "grid")

name_txt = Text(box_of_wisdom, grid = [0, 0], text = "Họ và tên: ")
school_txt = Text(box_of_wisdom, grid = [0, 1], text = "Chọn cấp học:")
height_txt = Text(box_of_wisdom, grid = [0, 2], text = "Chọn chiều cao (cm): ")
email_txt = Text(box_of_wisdom, grid = [0, 3], text = "Email: ")
phone_num_txt = Text(box_of_wisdom, grid = [0, 4], text = "Số điện thoại: ")
gender_txt = Text(box_of_wisdom, grid = [0, 5], text = "Giới tính: ")

name = TextBox(box_of_wisdom, grid = [1, 0], width = 30)
school = Combo(box_of_wisdom, grid = [1, 1], options = ["Tiểu học", "THCS", "THPT", "Đại học"])
height = Slider(box_of_wisdom, grid = [1, 2], start = 150, end = 210)
email = TextBox(box_of_wisdom, grid = [1, 3], width = 40)
phone_num = TextBox(box_of_wisdom, grid = [1, 4], width = 10)
gender = ButtonGroup(box_of_wisdom, grid = [1, 5], options = ["Nam", "Nữ", "Khác"])

register_btn = PushButton(window, command = register, text = "Đăng ký")

window.display()