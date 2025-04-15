from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QListWidgetItem, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import requests
from bs4 import BeautifulSoup
import datetime
import pickle
import os
import pic_rc  # Thư viện ảnh thiết kế giao diện

class Ui_Newsboard(object):
    def setupUi(self, Newsboard): # Thiết lập giao diện người dùng
        Newsboard.setObjectName("Newsboard")
        Newsboard.resize(1366, 743)
        Newsboard.setFixedSize(1366, 743)
        self.centralwidget = QtWidgets.QWidget(Newsboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.background = QtWidgets.QScrollArea(self.centralwidget)
        self.background.setWidgetResizable(True)
        self.background.setObjectName("background")

        # Định nghĩa hình nền cho các thời điểm khác nhau trong ngày
        self.background_images = {
            "morning": ":/images/morning.jpg",
            "afternoon": ":/images/afternoon.jpg",
            "evening": ":/images/evening.jpg",
            "midnight": ":/images/midnight.jpg"
        }
        self.board_images = {
            "board2": ":/images/board2.png",
            "board3": ":/images/board3.png",
            "board4": ":/images/board4.png"
        }
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(11, 11, 1344, 695))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Thiết lập các nhãn thông tin thời tiết
        self.weather = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.weather.setGeometry(QtCore.QRect(20, 20, 740, 300))
        self.weather.setStyleSheet("border-image: url(:/images/board2.png); border-radius: 10px;")
        self.weather.setText("")
        self.weather.setObjectName("weather")

        self.Weathertoday = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Weathertoday.setGeometry(QtCore.QRect(560, 40, 180, 30))
        self.Weathertoday.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.Weathertoday.setObjectName("Weathertoday")

        self.weatherstatus = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.weatherstatus.setGeometry(QtCore.QRect(40, 230, 700, 70))
        self.weatherstatus.setStyleSheet("border-image: url(:/images/board0.png); border-radius: 10px;")
        self.weatherstatus.setObjectName("weatherstatus")

        self.wind = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wind.setGeometry(QtCore.QRect(40, 230, 140, 70))
        self.wind.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.wind.setText("")
        self.wind.setObjectName("wind")

        self.humidity = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.humidity.setGeometry(QtCore.QRect(180, 230, 140, 70))
        self.humidity.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.humidity.setText("")
        self.humidity.setObjectName("humidity")

        self.visibility = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.visibility.setGeometry(QtCore.QRect(320, 230, 140, 70))
        self.visibility.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.visibility.setText("")
        self.visibility.setObjectName("visibility")

        self.clouds = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.clouds.setGeometry(QtCore.QRect(460, 230, 140, 70))
        self.clouds.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.clouds.setText("")
        self.clouds.setObjectName("clouds")

        self.pressure = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pressure.setGeometry(QtCore.QRect(600, 230, 140, 70))
        self.pressure.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.pressure.setText("")
        self.pressure.setObjectName("pressure")

        self.weathericon = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.weathericon.setGeometry(QtCore.QRect(40, 90, 120, 120))
        self.weathericon.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.weathericon.setText("")
        self.weathericon.setObjectName("weathericon")

        self.temperature = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.temperature.setGeometry(QtCore.QRect(233, 90, 120, 120))
        self.temperature.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.temperature.setText("")
        self.temperature.setObjectName("temperature")

        self.description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.description.setGeometry(QtCore.QRect(427, 90, 120, 120))
        self.description.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.description.setText("")
        self.description.setObjectName("description")

        self.location = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.location.setGeometry(QtCore.QRect(620, 90, 120, 120))
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setStyleSheet("border-image: url(:/images/0.png); border-radius: 10px;")
        self.location.setText("")
        self.location.setObjectName("location")

        self.searchbar = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.searchbar.setGeometry(QtCore.QRect(40, 40, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setAccessibleDescription("")
        self.searchbar.setStyleSheet("border-image: url(:/images/board0.png); border-radius: 10px;")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")

        self.searchbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.searchbutton.setGeometry(QtCore.QRect(510, 40, 30, 30))
        self.searchbutton.setStyleSheet("border-image: url(:/images/searchicon.png); border-radius: 10px;")
        self.searchbutton.setText("")
        self.searchbutton.setObjectName("searchbutton")

        # Thiết lập nhãn thông tin giá vàng
        self.goldprice = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.goldprice.setGeometry(QtCore.QRect(440, 480, 320, 223))
        self.goldprice.setStyleSheet("border-image: url(:/images/board0.png);")
        self.goldprice.setObjectName("goldprice")

        self.goldpricecontent = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.goldpricecontent.setGeometry(QtCore.QRect(460, 500, 280, 183))
        self.goldpricecontent.setStyleSheet("border-image: url(:/images/board0.png);")
        self.goldpricecontent.setObjectName("goldpricecontent")

        self.updateButton = QtWidgets.QPushButton("Update", self.scrollAreaWidgetContents) # Nút update giá vàng
        self.updateButton.setGeometry(QtCore.QRect(570, 650, 61, 21))
        self.updateButton.setStyleSheet("border-image: url(:/images/board1.png);")
        self.updateButton.setText("Update")
        self.updateButton.setObjectName("updateButton")
        

        # Thiết lập danh sách công việc và các nút liên quan
        self.todolist = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.todolist.setGeometry(QtCore.QRect(20, 340, 400, 363))
        self.todolist.setStyleSheet("border-image: url(:/images/board2.png);")
        self.todolist.setText("")
        self.todolist.setObjectName("todolist")

        self.tasks_file = "tasks.pkl"

        self.todo_list_widget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.todo_list_widget.setGeometry(QtCore.QRect(40, 430, 360, 230))
        self.todo_list_widget.setObjectName("todo_list_widget")
        self.todo_list_widget.setStyleSheet("border-image: url(:/images/board0.png);")
        self.todo_list_widget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.ToDo_List = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ToDo_List.setGeometry(QtCore.QRect(100, 350, 240, 40))
        self.ToDo_List.setStyleSheet("border-image: url(:/images/0.png);")
        self.ToDo_List.setObjectName("ToDo_List")

        self.new_task_input = QLineEdit(self.scrollAreaWidgetContents)
        self.new_task_input.setGeometry(QtCore.QRect(40, 400, 360, 30))
        self.new_task_input.setObjectName("new_task_input")
        self.new_task_input.setPlaceholderText("Add more task")
        self.new_task_input.setStyleSheet("border-image: url(:/images/board0.png); padding-left: 5px; color: #999;")
        
        self.add_task_button = QPushButton(self.scrollAreaWidgetContents)
        self.add_task_button.setGeometry(QtCore.QRect(370, 400, 30, 30))
        self.add_task_button.setObjectName("add_task_button")
        self.add_task_button.setText("↵")
        self.add_task_button.setStyleSheet("border-image: url(:/images/board0.png);")

        self.delete_task_button = QPushButton(self.scrollAreaWidgetContents)
        self.delete_task_button.setGeometry(QtCore.QRect(290, 668, 50, 23))
        self.delete_task_button.setObjectName("delete_task_button")
        self.delete_task_button.setText("Delete")
        self.delete_task_button.setStyleSheet("border-image: url(:/images/board0.png);")

        self.clear_tasks_button = QPushButton(self.scrollAreaWidgetContents)
        self.clear_tasks_button.setGeometry(QtCore.QRect(350, 668, 50, 23))
        self.clear_tasks_button.setObjectName("clear_tasks_button")
        self.clear_tasks_button.setText("Clear")
        self.clear_tasks_button.setStyleSheet("border-image: url(:/images/board0.png);")

        # Thiết lập nhãn thời gian
        self.time = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.time.setGeometry(QtCore.QRect(440, 340, 320, 120))
        self.time.setStyleSheet("border-image: url(:/images/board0.png);\n"
                                "font-size: 3px;")
        self.time.setObjectName("time")
        
        # Cập nhật thời gian định kỳ bằng QTimer
        timer = QtCore.QTimer(self.scrollAreaWidgetContents)
        timer.timeout.connect(self.update_time)
        timer.start(1000)  

        # Thiết lập các nhãn thông tin tin tức
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(780, 20, 544, 683))
        self.label.setStyleSheet("border-image: url(:/images/board2.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.Newstoday = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Newstoday.setGeometry(QtCore.QRect(930, 35, 245, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Newstoday.setFont(font)
        self.Newstoday.setStyleSheet("border-image: url(:/images/0.png);")
        self.Newstoday.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.Newstoday.setObjectName("Newstoday")

        self.newsload = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.newsload.setGeometry(QtCore.QRect(800, 90, 504, 593))
        self.newsload.setStyleSheet("border-image: url(:/images/board0.png);")
        self.newsload.setWidgetResizable(True)
        self.newsload.setObjectName("newsload")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 504, 593))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.newsload.setWidget(self.scrollAreaWidgetContents_2)

        self.reloadbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.reloadbutton.setGeometry(QtCore.QRect(880, 35, 40, 40))
        self.reloadbutton.setStyleSheet("border-image: url(:/images/reloadbutton.png);")
        self.reloadbutton.setText("")
        self.reloadbutton.setObjectName("reloadbutton")

        self.seemorebutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.seemorebutton.setGeometry(QtCore.QRect(1185, 35, 40, 40))
        self.seemorebutton.setStyleSheet("border-image: url(:/images/seemore.png);")
        self.seemorebutton.setObjectName("seemorebutton")

        # Đưa các widget lên trên cùng
        self.label.raise_()
        self.weather.raise_()
        self.Weathertoday.raise_()
        self.searchbar.raise_()
        self.searchbutton.raise_()
        self.todolist.raise_()
        self.ToDo_List.raise_()
        self.todo_list_widget.raise_()
        self.new_task_input.raise_()
        self.add_task_button.raise_()
        self.delete_task_button.raise_()
        self.clear_tasks_button.raise_()
        self.time.raise_()
        self.reloadbutton.raise_()
        self.seemorebutton.raise_()
        self.weatherstatus.raise_()
        self.wind.raise_()
        self.humidity.raise_()
        self.visibility.raise_()
        self.clouds.raise_()
        self.pressure.raise_()
        self.weathericon.raise_()
        self.temperature.raise_()
        self.description.raise_()
        self.location.raise_()
        self.Newstoday.raise_()
        self.newsload.raise_()

        # Thiết lập cấu trúc và bố trí giao diện chính của ứng dụng
        self.background.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.background, 0, 0, 1, 1)
        Newsboard.setCentralWidget(self.centralwidget)

        Newsboard.closeEvent = self.closeEvent # Kết nối sự kiện đóng ứng dụng

        # Gọi phương thức để cập nhật hình nền, giao diện của ứng dụng dựa trên thời gian hiện tại trong ngày
        self.update_background_by_time()
        self.update_board_image()

        self.retranslateUi(Newsboard) # Gọi phương thức để dịch lại các văn bản giao diện người dùng
        QtCore.QMetaObject.connectSlotsByName(Newsboard) # Tự động kết nối các tín hiệu và slot theo tên trong đối tượng Newsboard

        # Kết nối sự kiện nhấn Enter khi tìm kiếm với phương thức on_search_pressed   
        self.searchbar.returnPressed.connect(self.on_search_pressed)
        # Kết nối sự kiện nhấn nút searchbutton với phương thức on_search_pressed
        self.searchbutton.pressed.connect(self.on_search_pressed)
        # Kết nối sự kiện thả nút searchbutton với phương thức on_search_released
        self.searchbutton.released.connect(self.on_search_released)

        # Kết nối sự kiện click nút updatebutton với phương thức display_goldprice
        self.updateButton.clicked.connect(self.display_goldprice)

        # Kết nối sự kiện nhấn nút reloadbutton với phương thức on_reload_pressed
        self.reloadbutton.pressed.connect(self.on_reload_pressed)
        # Kết nối sự kiện thả nút reloadbutton với phương thức on_reload_released
        self.reloadbutton.released.connect(self.on_reload_released)
        # Kết nối sự kiện click (nhấn và thả) nút reloadbutton với phương thức refresh_news
        self.reloadbutton.clicked.connect(self.refresh_news)

        # Kết nối sự kiện nhấn nút seemorebutton với phương thức on_seemore_pressed
        self.seemorebutton.pressed.connect(self.on_seemore_pressed)
        # Kết nối sự kiện thả nút seemorebutton với phương thức on_seemore_released
        self.seemorebutton.released.connect(self.on_seemore_released)
        # Kết nối sự kiện click (nhấn và thả) nút seemorebutton với phương thức load_more_news
        self.seemorebutton.clicked.connect(self.load_more_news)

        self.display_weather()  # Hiển thị thông tin thời tiết mặc định khi giao diện được khởi tạo
        self.displayed_news_links = []  # Danh sách lưu trữ các liên kết tin đã hiển thị
        self.display_news()  # Hiển thị thông tin thời tiết mặc định khi giao diện được khởi tạo
        self.display_goldprice()  # Fetch gold price on setup
        
        self.load_tasks()  # Gọi phương thức load_tasks để tải danh sách các công việc từ file khi giao diện được khởi tạo

        self.update_time() # Gọi phương thức update_time để cập nhật thời gian khi giao diện được khởi tạo

        # Kết nối sự kiện thay đổi văn bản của searchbar với hàm search_location_suggestions
        self.searchbar.textChanged.connect(self.search_location_suggestions)

        # Khởi tạo QCompleter để cung cấp gợi ý cho searchbar
        self.completer = QtWidgets.QCompleter()
        self.searchbar.setCompleter(self.completer)

        # Kết nối sự kiện click của nút add_task_button với phương thức add_task
        self.add_task_button.clicked.connect(self.add_task)
        # Kết nối sự kiện click của nút delete_task_button với phương thức delete_task
        self.delete_task_button.clicked.connect(self.delete_task)
        # Kết nối sự kiện click của nút clear_tasks_button với phương thức clear_tasks
        self.clear_tasks_button.clicked.connect(self.clear_tasks)

        # Kết nối sự kiện nhấn phím Enter trong new_task_input với phương thức add_task
        self.new_task_input.returnPressed.connect(self.add_task)

        # Gắn sự kiện double click vào item trong todo_list_widget để đánh dấu công việc đã hoàn thành
        self.todo_list_widget.itemDoubleClicked.connect(self.toggle_task_completion)

    def retranslateUi(self, Newsboard): # Dịch lại giao diện người dùng
        _translate = QtCore.QCoreApplication.translate
        # Đặt tiêu đề của cửa sổ chính của ứng dụng
        Newsboard.setWindowTitle(_translate("Newsboard", "News Board"))
        # Đặt văn bản gợi ý trong thanh tìm kiếm
        self.searchbar.setPlaceholderText(_translate("Newsboard", "Enter location"))

        # Đặt văn bản và kiểu dáng cho phần NEWS TODAY
        self.Newstoday.setText(_translate("Newsboard", "NEWS TODAY"))
        self.Newstoday.setAlignment(QtCore.Qt.AlignCenter)
        self.Newstoday.setStyleSheet("text-transform: uppercase; font-weight: bold; font-size: 12pt; border-image: url(:/images/board0.png);")

        # Đặt văn bản và kiểu dáng cho phần WEATHER TODAY
        self.Weathertoday.setText(_translate("Newsboard", "WEATHER TODAY"))
        self.Weathertoday.setAlignment(QtCore.Qt.AlignCenter)
        self.Weathertoday.setStyleSheet("text-transform: uppercase; font-weight: bold; font-size: 12pt; border-image: url(:/images/board0.png);")

        # Đặt văn bản và kiểu dáng cho phần ToDO LIST
        self.ToDo_List.setText(_translate("Newsboard", "TODO LIST"))
        self.ToDo_List.setAlignment(QtCore.Qt.AlignCenter)
        self.ToDo_List.setStyleSheet("text-transform: uppercase; font-weight: bold; font-size: 12pt; border-image: url(:/images/board0.png);")

    def update_background_image(self): # Cập nhật ảnh nền 
        # Lấy thời gian hiện tại
        current_time = datetime.datetime.now().time()

        # Xác định hình nền dựa trên thời gian
        if current_time >= datetime.time(4, 0) and current_time < datetime.time(9, 0):
            background_image = self.background_images["morning"]
        elif current_time >= datetime.time(9, 0) and current_time < datetime.time(16, 0):
            background_image = self.background_images["afternoon"]
        elif current_time >= datetime.time(16, 0) and current_time < datetime.time(18, 0):
            background_image = self.background_images["evening"]
        else:
            background_image = self.background_images["midnight"]

        # Cập nhật hình nền
        self.background.setStyleSheet(f"border-image: url({background_image}); border-radius: 10px;")

    def update_board_image(self): # Cập nhật các bảng thông báo 
        # Lấy thời gian hiện tại
        current_time = datetime.datetime.now().time()

        # Xác định hình border dựa trên thời gian
        if current_time >= datetime.time(4, 0) and current_time < datetime.time(9, 0):
            board_image = self.board_images["board2"]
        elif current_time >= datetime.time(9, 0) and current_time < datetime.time(18, 0):
            board_image = self.board_images["board3"]
        else:
            board_image = self.board_images["board4"]

        # Cập nhật border image cho các phần tử có sử dụng border image
        self.weather.setStyleSheet(f"border-image: url({board_image});")
        self.todolist.setStyleSheet(f"border-image: url({board_image});")
        self.label.setStyleSheet(f"border-image: url({board_image});")
        self.time.setStyleSheet(f"border-image: url({board_image});")
        self.goldprice.setStyleSheet(f"border-image: url({board_image});")
        
    def update_background_by_time(self): # Cập nhật giao diện theo thời gian trong ngày
        # Cập nhật hình nền và hình border dựa trên thời gian
        self.update_background_image()
        self.update_board_image()

    def display_weather(self): # Hiển thị thời tiết
        # Lấy tên thành phố từ thanh tìm kiếm
        city = self.searchbar.text()
        if not city:
            city = "Ho Chi Minh"  # Nếu không có tên thành phố nào được nhập, sử dụng "Ho Chi Minh" mặc định
        api_key = "e214ca1e9729fe7fd0af27f81849b50b"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            # Gửi yêu cầu API để lấy dữ liệu thời tiết từ OpenWeatherMap
            response = requests.get(url)
            data = response.json()
            city_name = data["name"]  # Lấy tên thành phố từ dữ liệu trả về
            country = data["sys"]["country"]  # Lấy tên quốc gia từ dữ liệu trả về
            temperature_kelvin = data["main"]["temp"]
            temperature_celsius = temperature_kelvin - 273.15

            # Chuyển màu và thêm icon dựa trên nhiệt độ
            if temperature_celsius > 28:
                # Nếu nhiệt độ cao hơn 25°C, sử dụng màu và biểu tượng tương ứng
                self.temperature.setStyleSheet("border-image: url(:/images/board0.png); color: rgb(179, 119, 41);")
                self.temperature.setText(f"<div align='center'><span style='font-size: 16pt;'><b>{temperature_celsius:.2f}°C</span></div>" 
                                        f"<div align='center'><span style='font-size: 16pt;'>🥵</span></div>")
            elif 25 <= temperature_celsius <= 28:
                # Nếu nhiệt độ nằm trong khoảng từ 22°C đến 25°C, sử dụng màu và biểu tượng tương ứng
                self.temperature.setStyleSheet("border-image: url(:/images/board0.png); color: rgb(71, 179, 41);")
                self.temperature.setText(f"<div align='center'><span style='font-size: 16pt;'><b>{temperature_celsius:.2f}°C</span></div>" 
                                        f"<div align='center'><span style='font-size: 16pt;'>😄</span></div>")
            else:
                # Nếu nhiệt độ thấp hơn 22°C, sử dụng màu và biểu tượng tương ứng
                self.temperature.setStyleSheet("border-image: url(:/images/board0.png); color: rgb(41, 163, 179);")
                self.temperature.setText(f"<div align='center'><span style='font-size: 16pt;'><b>{temperature_celsius:.2f}°C</span></div>" 
                                        f"<div align='center'><span style='font-size: 16pt;'>🥶</span></div>")

            # Hiển thị thông tin thời tiết và các chỉ số khác
            weather_description = data["weather"][0]["description"]
            feels_like_kelvin = data["main"]["feels_like"]
            feels_like_celsius = feels_like_kelvin - 273.15
            temp_min_kelvin = data["main"]["temp_min"]
            temp_min_celsius = temp_min_kelvin - 273.15
            temp_max_kelvin = data["main"]["temp_max"]
            temp_max_celsius = temp_max_kelvin - 273.15
            visibility = data["visibility"]
            wind_speed = data["wind"]["speed"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            weather_icon_id = data["weather"][0]["icon"]
            weather_icon_url = f"http://openweathermap.org/img/wn/{weather_icon_id}.png"
            icon_data = requests.get(weather_icon_url).content
            weather_icon_pixmap = QtGui.QPixmap()
            weather_icon_pixmap.loadFromData(icon_data)
            self.weathericon.setPixmap(weather_icon_pixmap)
            self.weathericon.setScaledContents(True)
            self.weathericon.setAlignment(QtCore.Qt.AlignCenter)
            self.location.setStyleSheet("border-image: url(:/images/board0.png);")
            self.location.setText(f"<div align='center'><span style='font-size: 10pt;'> {city_name}" 
                                f"<div align='center'><span style='font-size: 10pt;'> {country}</span></div>")
            self.description.setStyleSheet("border-image: url(:/images/board0.png);")
            self.description.setText(f"<div align='center'><span style='font-size: 8pt;'> {weather_description}</span></div>"
                                f"<div align='center'><span style='font-size: 8pt;'>Feels Like: {feels_like_celsius:.2f}°C</span></div>"
                                f"<div align='center'><span style='font-size: 8pt;'>Min Temp: {temp_min_celsius:.2f}°C</span></div>"
                                f"<div align='center'><span style='font-size: 8pt;'>Max Temp: {temp_max_celsius:.2f}°C</span></div>")
            self.visibility.setStyleSheet("border-image: url(:/images/board0.png);")
            self.visibility.setText(f"<div align='center'><span style='font-size: 12pt;'>Visibility:</span></div>" 
                                f"<div align='center'><span style='font-size: 12pt;'>👁️{visibility}m</span></div>")
            self.wind.setStyleSheet("border-image: url(:/images/board0.png);")
            self.wind.setText(f"<div align='center'><span style='font-size: 12pt;'>Wind Speed:</span></div>" 
                        f"<div align='center'><span style='font-size: 12pt;'>🌬️{wind_speed}m/s</span></div>")
            self.humidity.setStyleSheet("border-image: url(:/images/board0.png);")
            self.humidity.setText(f"<div align='center'><span style='font-size: 12pt;'>Humidity:</span></div>" 
                            f"<div align='center'><span style='font-size: 12pt;'>💧{humidity}%</span></div>")
            self.clouds.setStyleSheet("border-image: url(:/images/board0.png);")
            self.clouds.setText(f"<div align='center'><span style='font-size: 12pt;'>Clouds:</span></div>"
                            f"<div align='center'><span style='font-size: 12pt;'>☁️{data['clouds']['all']}%</span></div>")
            self.pressure.setStyleSheet("border-image: url(:/images/board0.png);")
            self.pressure.setText(f"<div align='center'><span style='font-size: 12pt;'>Pressure:</span></div>"
                            f"<div align='center'><span style='font-size: 12pt;'>🌀{pressure}hPa</span></div>")
        except Exception as e:
            # Xử lý nếu không thể lấy dữ liệu thời tiết
            print("Failed to fetch weather data:", e)
            # Hiển thị "N/A" nếu không thể lấy dữ liệu
            self.temperature.setText("<div align='center'><span style='font-size: 20pt; color: black;'>N/A</span></div>")
            self.description.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.location.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.visibility.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.wind.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.humidity.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.clouds.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.pressure.setText("<div align='center'><span style='font-size: 8pt;'>N/A</span></div>")
            self.weathericon.clear()

    def search_location_suggestions(self, text): # Gợi ý tìm kiếm địa điểm 
        # Tìm kiếm gợi ý địa điểm dựa trên văn bản nhập vào từ thanh tìm kiếm
        if len(text) < 3:
            return
        api_key = "e214ca1e9729fe7fd0af27f81849b50b"
        url = f"http://api.openweathermap.org/data/2.5/find?q={text}&type=like&appid={api_key}"
        try:
            # Gửi yêu cầu API để lấy danh sách các địa điểm gợi ý từ OpenWeatherMap
            response = requests.get(url)
            data = response.json()
            cities = [item["name"] for item in data["list"]]
            # Tạo một mô hình cho gợi ý địa điểm và gán nó cho completer
            model = QtGui.QStandardItemModel()
            for city in cities:
                item = QtGui.QStandardItem(city)
                model.appendRow(item)
            self.completer.setModel(model)
        except Exception as e:
            print("An error occurred while fetching location suggestions:", e)

    def display_goldprice(self):
        api_url = 'https://api.api-ninjas.com/v1/goldprice'
        headers = {'X-Api-Key': 'pNi7R2ZMZkt0uk7MpMVrFg==I2tLtFq7f8NC02sS'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == requests.codes.ok:
            data = response.json()
            price = data['price']
            updated_timestamp = data['updated']
            updated_datetime = datetime.datetime.fromtimestamp(updated_timestamp)

            self.goldpricecontent.setText(
                f"<div align='center'><span style='font-size: 12pt;'><b>GOLD PRICE TODAY</b></span></div>"
                f"<div align='center'><span style='font-size: 8pt; color: green;'>Current gold price: {price} USD/ounce</span></div>"
                f"<div align='center'><span style='font-size: 8t;'>Last updated: {updated_datetime}</span></div>"
                f"<div align='center'><span style='font-size: 8pt;'>Source: Chicago Mercantile Exchange (CME)</span></div>"
            )
        else:
            self.goldpricecontent.setText(f"<p style='font-size: 8pt;'>Error fetching gold price: {response.status_code}</p>")

    def toggle_task_completion(self, item): # Trạng thái hoàn thành của công việc
        # Đảo ngược trạng thái đã hoàn thành của task khi double click
        item.setCheckState(QtCore.Qt.Checked if item.checkState() == QtCore.Qt.Unchecked else QtCore.Qt.Unchecked)

    def add_task(self): # Thêm công việc
        # Thêm task với checkbox
        task_text = self.new_task_input.text()
        if task_text:
            task_item = QListWidgetItem(task_text, self.todo_list_widget)
            task_item.setFlags(task_item.flags() | QtCore.Qt.ItemIsUserCheckable)  # Cho phép người dùng đánh dấu task
            task_item.setCheckState(QtCore.Qt.Unchecked)  # Task mặc định chưa được hoàn thành
            self.todo_list_widget.addItem(task_item)
            self.new_task_input.clear()

    def delete_task(self): # Xóa công việc
        # Xóa các task đã chọn
        selected_items = self.todo_list_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                self.todo_list_widget.takeItem(self.todo_list_widget.row(item))

    def clear_tasks(self): # Xóa toàn bộ công việc
        # Hiển thị hộp thoại xác nhận
        confirm_dialog = QMessageBox()
        confirm_dialog.setStyleSheet("border-image: url(:/images/board0.png);")
        confirm_dialog.setWindowTitle("Confirm")
        confirm_dialog.setText("Are you sure you want to delete all tasks?")
        confirm_dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        # Căn giữa chữ thông báo
        confirm_dialog.setTextFormat(QtCore.Qt.RichText)
        confirm_dialog.setText("<div style='text-align: center;'>Are you sure you want to delete all tasks?</div>")
        
        # Thiết lập hình ảnh nền cho các nút trong hộp thoại
        confirm_dialog.button(QMessageBox.Ok).setStyleSheet("border-image: url(:/images/board0.png);")
        confirm_dialog.button(QMessageBox.Cancel).setStyleSheet("border-image: url(:/images/board0.png);")

        result = confirm_dialog.exec_()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng

        if result == QMessageBox.Ok:  # Nếu người dùng chọn OK
            self.todo_list_widget.clear()  # Xóa toàn bộ task
            self.save_tasks()  # Lưu danh sách task sau khi xóaa
  
    def save_tasks(self): # Tự động lưu công việc 
        # Lưu danh sách task vào file pickle
        tasks = [{"text": self.todo_list_widget.item(i).text(),
                  "checked": self.todo_list_widget.item(i).checkState()} for i in range(self.todo_list_widget.count())]
        with open(self.tasks_file, 'wb') as file:
            pickle.dump(tasks, file)

    def load_tasks(self): # Tải danh sách công việc khi mở giao diện
        # Tải danh sách task từ file pickle
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'rb') as file:
                tasks = pickle.load(file)
            self.todo_list_widget.clear()
            if isinstance(tasks, list):  # Kiểm tra xem dữ liệu tải có phải là danh sách không
                for task in tasks:
                    if isinstance(task, str):  # Kiểm tra xem mỗi mục trong danh sách có phải là một chuỗi không
                        task_item = QListWidgetItem(task, self.todo_list_widget)
                        task_item.setFlags(task_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        task_item.setCheckState(QtCore.Qt.Unchecked)  # Mặc định task chưa được hoàn thành
                        self.todo_list_widget.addItem(task_item)
                    elif isinstance(task, dict):  # Nếu mục là một từ điển
                        task_text = task.get("text", "")  # Lấy văn bản của task từ dữ liệu tải
                        checked = task.get("checked", QtCore.Qt.Unchecked)  # Lấy trạng thái đã hoàn thành của task từ dữ liệu tải
                        task_item = QListWidgetItem(task_text, self.todo_list_widget)
                        task_item.setFlags(task_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        task_item.setCheckState(QtCore.Qt.Checked if checked == QtCore.Qt.Checked else QtCore.Qt.Unchecked)
                        self.todo_list_widget.addItem(task_item)
                    else:
                        print("Invalid task format:", task)
            else:
                print("Invalid tasks data format:", tasks)

    def closeEvent(self, event): # Sự kiện đóng giao diện để tự động lưu công việc
        # Lưu danh sách task khi giao diện được đóng
        self.save_tasks()

    def update_time(self): # Cập nhật thời gian
        # Lấy thời gian hiện tại
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # Lấy ngày hiện tại
        current_date = datetime.datetime.now().strftime("%A, %d/%m/%Y")
        
        # Cập nhật thời gian và ngày hiện tại lên giao diện
        self.time.setText("<html><head/><body><p align='center'>"
                    f"<span style='font-size:36pt; color: rgba(0, 0, 255, 0.6);'><b>{current_time}</span><br/>"
                    f"<span style='font-size:16pt;'>{current_date}</span></p></body></html>")

    def get_news(self, limit=10, exclude_links=[]): # Lấy tin tức
        try:
            website_url = "https://tuoitre.vn/tin-moi-nhat.htm"  # URL của trang web cần lấy tin tức
            
            # Gửi yêu cầu GET đến trang web
            response = requests.get(website_url)
            response.raise_for_status()
            
            # Phân tích HTML sử dụng BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Tìm tất cả các thẻ hình ảnh trong trang
            img_tags = soup.find_all('img')
            
            # Lấy URL của các hình ảnh
            img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

            # Tìm tất cả các tiêu đề tin tức
            titles = soup.find_all('a', class_='box-category-link-title')
            
            # Lấy văn bản của các tiêu đề
            title_texts = [title.text.strip() for title in titles]

            # Lấy liên kết của các bài báo
            article_links = ["https://tuoitre.vn" + title['href'] for title in titles]

            # Tìm tất cả các mô tả của các bài báo
            descriptions = soup.find_all('p', class_='box-category-sapo')
            
            # Lấy văn bản mô tả
            description_texts = [desc.text.strip() for desc in descriptions]

            # Bỏ qua các hình ảnh không cần thiết
            img_urls = img_urls[2:]
            
            # Gom các thông tin lại thành list của tuples
            news = list(zip(img_urls, title_texts, article_links, description_texts))
            
            # Loại bỏ các liên kết đã hiển thị
            news = [item for item in news if item[2] not in exclude_links]

            # Trả về số lượng tin tức giới hạn theo đối số 'limit'
            return news[:limit]
        except Exception as e:
            # Xử lý ngoại lệ nếu có lỗi xảy ra
            print("An error occurred while fetching news data:", e)
            
            # Trả về danh sách rỗng nếu có lỗi
            return []

    def display_news(self): # Hiển thị tin tức 
        # Lấy dữ liệu tin tức mới
        news = self.get_news()  
        
        # Tạo một layout dọc cho các mục tin tức bên trong widget cuộn
        layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)  
        
        # Khởi tạo một danh sách rỗng để lưu các liên kết của các bài báo đã hiển thị
        self.displayed_news_links = []  

        # Lặp qua từng mục tin tức
        for img_url, title, article_link, description in news:  
            # Thêm liên kết của bài báo vào danh sách các liên kết đã hiển thị
            self.displayed_news_links.append(article_link)  
            
            # Tạo một widget mới cho mục tin tức
            widget = QtWidgets.QWidget()  
            
            # Đặt ảnh nền cho widget
            widget.setStyleSheet("border-image: url(:/images/0.png);")  
            
            # Tạo một layout ngang cho nội dung của widget
            inner_layout = QtWidgets.QHBoxLayout(widget)  
            
            try:
                # Tải hình ảnh từ URL
                pixmap = QtGui.QPixmap()  
                pixmap.loadFromData(requests.get(img_url).content)  
                
                # Kiểm tra xem hình ảnh có hợp lệ và không rỗng
                if not pixmap.isNull():  
                    # Chỉnh kích thước hình ảnh về chiều rộng 150 pixel
                    pixmap = pixmap.scaledToWidth(150)  
                    
                    # Tạo một label để hiển thị hình ảnh
                    label = QtWidgets.QLabel()  
                    label.setPixmap(pixmap)  
                    label.setAlignment(QtCore.Qt.AlignLeft)  
                    
                    # Thêm label hình ảnh vào layout ngang
                    inner_layout.addWidget(label)  
            except Exception as e:
                # In thông báo lỗi nếu không tải được hình ảnh
                print("Error loading image:", e)  

            # Tạo một layout dọc cho tiêu đề và mô tả
            info_layout = QtWidgets.QVBoxLayout()  
            
            # Thêm layout dọc vào layout ngang
            inner_layout.addLayout(info_layout)  

            # Tạo một label cho tiêu đề tin tức với liên kết có thể nhấp
            title_label = QtWidgets.QLabel(f"<a href='{article_link}' style='color: blue; text-decoration: none;'>{title}</a>")  
            title_label.setTextFormat(QtCore.Qt.RichText)  
            
            # Đặt font chữ cho label tiêu đề
            font = QtGui.QFont("Roboto", 10)  
            font.setBold(True)  
            title_label.setFont(font)  
            
            # Cho phép mở liên kết tiêu đề trong trình duyệt ngoài
            title_label.setOpenExternalLinks(True)  
            
            # Thêm label tiêu đề vào layout dọc
            info_layout.addWidget(title_label)  

            # Tạo một label cho mô tả tin tức
            description_label = QtWidgets.QLabel(description)  

            # Đặt chiều rộng tối thiểu cho label mô tả
            description_label.setMinimumWidth(title_label.sizeHint().width())

            description_label.setWordWrap(True)  
            
            # Đặt font chữ cho label mô tả
            font = QtGui.QFont("Roboto", 8)  
            description_label.setFont(font)  
            description_label.setAlignment(QtCore.Qt.AlignLeft)  
            
            # Thêm label mô tả vào layout dọc, căn trái
            info_layout.addWidget(description_label, alignment=QtCore.Qt.AlignLeft)  

            # Thêm một khoảng trống có thể co giãn vào layout ngang để điều chỉnh khoảng cách
            inner_layout.addStretch(1)  
            
            # Thêm widget tin tức vào layout dọc chính
            layout.addWidget(widget)  
            
            # Thêm một khoảng trống có thể co giãn vào layout dọc chính để điều chỉnh khoảng cách
            layout.addStretch()  

        # Nếu có 20 mục tin tức trở lên, vô hiệu hóa nút 'Xem thêm'
        if len(news) >= 15:  
            self.seemorebutton.setEnabled(False)
 
    def load_more_news(self): # Tải thêm tin tức
        # Kiểm tra xem nút 'Xem thêm' có đang được kích hoạt không
        if not self.seemorebutton.isEnabled():
            return  # Nếu không, không làm gì cả và thoát khỏi phương thức
        
        # Lấy thêm tin tức mới (5 tin tức) mà chưa được hiển thị trước đó
        additional_news = self.get_news(5, exclude_links=self.displayed_news_links)
        
        # Hiển thị các tin tức mới
        self.display_additional_news(additional_news)  # Gọi phương thức để hiển thị các tin tức mới

    def display_additional_news(self, additional_news): # Hiển thị tin tức mới 
        # Lấy layout hiện tại của widget để thêm tin tức mới vào
        layout = self.newsload.widget().layout()  

        # Lặp qua từng mục tin tức bổ sung
        for img_url, title, article_link, description in additional_news:  
            # Thêm liên kết của bài báo vào danh sách các liên kết đã hiển thị
            self.displayed_news_links.append(article_link)  
            
            # Tạo một widget mới cho mục tin tức
            widget = QtWidgets.QWidget()  
            
            # Đặt ảnh nền cho widget
            widget.setStyleSheet("border-image: url(:/images/0.png);")  
            
            # Tạo một layout ngang cho nội dung của widget
            inner_layout = QtWidgets.QHBoxLayout(widget)  
            
            try:
                # Tải hình ảnh từ URL
                pixmap = QtGui.QPixmap()  
                pixmap.loadFromData(requests.get(img_url).content)  
                
                # Kiểm tra xem hình ảnh có hợp lệ và không rỗng
                if not pixmap.isNull():  
                    # Chỉnh kích thước hình ảnh về chiều rộng 150 pixel
                    pixmap = pixmap.scaledToWidth(150)  
                    
                    # Tạo một label để hiển thị hình ảnh
                    label = QtWidgets.QLabel()  
                    label.setPixmap(pixmap)  
                    label.setAlignment(QtCore.Qt.AlignLeft)  
                    
                    # Thêm label hình ảnh vào layout ngang
                    inner_layout.addWidget(label)  
            except Exception as e:
                # In thông báo lỗi nếu không tải được hình ảnh
                print("An error occurred while loading image:", e)  

            # Tạo một layout dọc cho tiêu đề và mô tả
            info_layout = QtWidgets.QVBoxLayout()  
            
            # Thêm layout dọc vào layout ngang
            inner_layout.addLayout(info_layout)  

            # Tạo một label cho tiêu đề tin tức với liên kết có thể nhấp
            title_label = QtWidgets.QLabel(f"<a href='%s' style='color: blue; text-decoration: none;'>%s</a>" % (article_link, title))  
            title_label.setTextFormat(QtCore.Qt.RichText)  
            
            # Đặt font chữ cho label tiêu đề
            font = QtGui.QFont("Roboto", 10)  
            font.setBold(True)  
            title_label.setFont(font)  
            
            # Cho phép mở liên kết tiêu đề trong trình duyệt ngoài
            title_label.setOpenExternalLinks(True)  
            
            # Thêm label tiêu đề vào layout dọc
            info_layout.addWidget(title_label)  

            # Tạo một label cho mô tả tin tức
            description_label = QtWidgets.QLabel(description)  

            # Đặt chiều rộng tối thiểu cho label mô tả
            description_label.setMinimumWidth(title_label.sizeHint().width())

            description_label.setWordWrap(True)  
            
            # Đặt font chữ cho label mô tả
            font = QtGui.QFont("Roboto", 8)  
            description_label.setFont(font)  
            description_label.setAlignment(QtCore.Qt.AlignLeft)  
            
            # Thêm label mô tả vào layout dọc, căn trái
            info_layout.addWidget(description_label, alignment=QtCore.Qt.AlignLeft)  

            # Thêm một khoảng trống có thể co giãn vào layout ngang để điều chỉnh khoảng cách
            inner_layout.addStretch(1)  
            
            # Thêm widget tin tức vào layout dọc chính
            layout.addWidget(widget)  
            
            # Thêm một khoảng trống có thể co giãn vào layout dọc chính để điều chỉnh khoảng cách
            layout.addStretch()  

    def clear_news_display(self): # Xóa các tin tức hiện tại
        # Xóa tất cả các widget hiện tại trong layout
        layout = self.scrollAreaWidgetContents_2.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
    def refresh_news(self): # Làm mới tin tức
        try:
            # Lấy tin tức mới
            new_news = self.get_news()

            # Xóa tin tức hiện tại khỏi giao diện
            self.clear_news_display()

            # Hiển thị tin tức mới
            self.update_displayed_news(new_news)
        except Exception as e:
            print("An error occurred while refreshing news:", e)

    def update_displayed_news(self, new_news): # Cập nhật hiển thị tin tức mới
        # Hiển thị tin tức mới trên giao diện
        self.display_additional_news(new_news)

    def on_search_pressed(self): # Sự kiện nhấn nhút tìm kiếm
        # Khi nút tìm kiếm được nhấn, thay đổi kiểu dáng của nút searchbutton
        self.searchbutton.setStyleSheet("border-image: url(:/images/searchiconclicked.png);")
        # Gọi hàm display_weather để hiển thị thông tin thời tiết cho thành phố đã nhập
        self.display_weather() 

    def on_search_released(self): # Sự kiện thả nút tìm kiếm
        # Khi nút tìm kiếm được thả, khôi phục lại kiểu dáng ban đầu của nút searchbutton
        self.searchbutton.setStyleSheet("border-image: url(:/images/searchicon.png);")
        # Khi nút tìm kiếm được nhấn, gọi hàm display_weather để hiển thị thông tin thời tiết cho thành phố đã nhập
        self.display_weather()

    def on_reload_pressed(self): # Sự kiện nhấn nút tải lại
        # Khi nút tải lại được nhấn, thay đổi kiểu dáng của nút reloadbutton
        self.reloadbutton.setStyleSheet("border-image: url(:/images/reloadbuttonclicked.png);")

    def on_reload_released(self): # Sự kiện thả nút tải lại
        # Khi nút tải lại được thả, khôi phục lại kiểu dáng ban đầu của nút reloadbutton
        self.reloadbutton.setStyleSheet("border-image: url(:/images/reloadbutton.png);")

    def on_seemore_pressed(self): # Sự kiện nhấn nút xem thêm
        # Khi nút xem thêm được nhấn, thay đổi kiểu dáng của nút seemorebutton
        self.seemorebutton.setStyleSheet("border-image: url(:/images/seemoreclicked.png);")

    def on_seemore_released(self): # Sự kiến thả nút xem thêm
        # Khi nút xem thêm được thả, khôi phục lại kiểu dáng ban đầu của nút seemorebutton
        self.seemorebutton.setStyleSheet("border-image: url(:/images/seemore.png);")

if __name__ == "__main__": # Chạy ứng dụng
    # Import module sys để tương tác với hệ thống
    import sys
    
    # Khởi tạo ứng dụng Qt
    app = QtWidgets.QApplication(sys.argv)
    
    # Tạo một QMainWindow mới để chứa giao diện người dùng của ứng dụng
    Newsboard = QtWidgets.QMainWindow()
    
    # Tạo một đối tượng giao diện người dùng từ lớp Ui_Newsboard
    ui = Ui_Newsboard()
    
    # Cấu hình giao diện người dùng cho QMainWindow Newsboard
    ui.setupUi(Newsboard)
    
    # Hiển thị QMainWindow Newsboard trên màn hình
    Newsboard.show()
    
    # Chạy vòng lặp chính của ứng dụng Qt và xác định kết thúc ứng dụng khi cửa sổ chính được đóng
    sys.exit(app.exec_())



