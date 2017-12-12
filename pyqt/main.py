from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import time
import datetime
import json
import pdb

# utc 转 local
def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
# local 转 utc
def local2utc(local_st):
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

# 字符串盘口转换成float
def handicap2float(handicap_name):
    if handicap_name == '':
        return 0
    handicap_name_first_letter = handicap_name[0]
    # 除了0球盘都有正负号
    if handicap_name_first_letter != '0':
        # 目前可能出现 +/- 0.5/1.0 or 0.5
        handicap_value_list = handicap_name.split('/')
        if len(handicap_value_list) == 1:
            handicap_value = float(handicap_value_list[0])
        else:
            handicap_value = (float(handicap_value_list[0]) + float(handicap_value_list[1])) / 2
        if handicap_name_first_letter == '-':
            handicap_value = -handicap_value
    else:
        handicap_value = float(handicap_name)
    return handicap_value

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.league_name = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 860, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.activated[str].connect(self.onActivated)   ##用来将combobox关联的函数
        self.pushButton.clicked.connect(self.toggleLanguage)   ##用来将切换中/英按钮关联的函数

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MatchBook_Analysis"))
        self.comboBox.setItemText(0, _translate("MainWindow", "select league"))
        self.comboBox.setItemText(1, _translate("MainWindow", "belgium"))
        self.comboBox.setItemText(2, _translate("MainWindow", "denmark"))
        self.comboBox.setItemText(3, _translate("MainWindow", "england"))
        self.comboBox.setItemText(4, _translate("MainWindow", "france"))
        self.comboBox.setItemText(5, _translate("MainWindow", "germany"))
        self.comboBox.setItemText(6, _translate("MainWindow", "italy"))
        self.comboBox.setItemText(7, _translate("MainWindow", "netherlands"))
        self.comboBox.setItemText(8, _translate("MainWindow", "portugal"))
        self.comboBox.setItemText(9, _translate("MainWindow", "russia"))
        self.comboBox.setItemText(10, _translate("MainWindow", "scotland"))
        self.comboBox.setItemText(11, _translate("MainWindow", "spain"))
        self.comboBox.setItemText(12, _translate("MainWindow", "turkey"))
        self.comboBox.setItemText(13, _translate("MainWindow", "argentina"))
        self.comboBox.setItemText(14, _translate("MainWindow", "australia"))
        self.comboBox.setItemText(15, _translate("MainWindow", "austria"))
        self.comboBox.setItemText(16, _translate("MainWindow", "switzerland"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "开赛时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "主队名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "盘口"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "客队名"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "主p净支持"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "主v净支持"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "主vp净支持"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "最后更新时间"))
        self.pushButton.setText(_translate("MainWindow", "切换中/英"))

    # 切换team name 中英文
    def toggleLanguage(self):
        if self.league_name == '' or self.tableWidget.rowCount() == 0:
            return
        f = open("teamName2chinese.json", encoding='utf-8')
        language_translate = json.load(f)
        # 先判断是否是中文
        is_chinnese = is_chinese(self.tableWidget.item(0, 1).text()[0])
        for i in range(self.tableWidget.rowCount()):
            current_host_name = self.tableWidget.item(i, 1).text()
            current_guest_name = self.tableWidget.item(i, 3).text()
            if is_chinnese:
                host_key = [x[0] for x in language_translate[self.league_name].items() if current_host_name in x[1]]
                guest_key = [x[0] for x in language_translate[self.league_name].items() if current_guest_name in x[1]]
                if len(host_key) != 0 and len(guest_key) != 0:
                    host_item = QtWidgets.QTableWidgetItem(host_key[0])
                    guest_guest = QtWidgets.QTableWidgetItem(guest_key[0])
                    self.tableWidget.setItem(i, 1, host_item)
                    self.tableWidget.setItem(i, 3, guest_guest)
            else:
                new_host_name = QtWidgets.QTableWidgetItem(language_translate[self.league_name][current_host_name])
                new_guest_name = QtWidgets.QTableWidgetItem(language_translate[self.league_name][current_guest_name])
                self.tableWidget.setItem(i, 1, new_host_name)
                self.tableWidget.setItem(i, 3, new_guest_name)

    def onActivated(self, text):  ##用来实现combobox关联的函数
        if text == 'select league':
            self.league_name = ''
            return
        self.league_name = text
        # 先连接至分析数据库获取上次所用分析表的时间
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL")
        db.setDatabaseName("match_" + text + "_analysis")
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root");  # set user name
        db.setPassword("");  # set user pwd
        if not db.open():
            # 打开失败
            return db.lastError()
        print("连接至 match_",text,"_analysis success!")
        # 创建QsqlQuery对象，用于执行sql语句
        query = QtSql.QSqlQuery()
        build_table = (
            "CREATE TABLE IF NOT EXISTS "' %s '""
            "(event_id VARCHAR(20) NOT NULL PRIMARY KEY,"
            "host_name VARCHAR(20) NOT NULL,"
            "guest_name VARCHAR(20) NOT NULL,"
            "handicap_name VARCHAR(20) NOT NULL,"
            "start_time VARCHAR(20) NOT NULL,"
            "host_price_net_support INT(4) NOT NULL DEFAULT 0,"
            "host_volume_net_support INT(4) NOT NULL DEFAULT 0,"
            "host_volume_price_net_support INT(4) NOT NULL DEFAULT 0,"
            "is_end INT(4) DEFAULT 0,"
            "handicap_result FLOAT(4),"  # 9 表示未知
            "last_updatetime VARCHAR(20))"
        )
        query.exec(build_table % 'analysis_result')
        # 查询出当前数据库中的所有表名
        query.exec('SELECT * FROM analysis_result')
        query.next()
        # 保存最后分析用的表上的时间，以便之后分析跳过用过的表
        if query.size() > 0:
            last_load_data_time = time.mktime(time.strptime(query.value(10), '%Y-%m-%d %H:%M:%S'))
        else:
            last_load_data_time = 0
        db.close()
        # 连接数据库
        db = QtSql.QSqlDatabase().addDatabase("QMYSQL")
        db.setDatabaseName("match_"+text)
        db.setHostName("127.0.0.1")  # set address
        db.setUserName("root")  # set user name
        db.setPassword("")  # set user pwd
        # 打开数据库
        if not db.open():
            # 打开失败
            return db.lastError()
        print("连接至 match_",text,"success!")

        # 保存比赛分析结果的字典，用event_id 映射单场比赛
        match_analysis_result = {}

        # 创建QsqlQuery对象，用于执行sql语句
        query = QtSql.QSqlQuery()
        # 查询出当前数据库中的所有表名
        query.exec('SHOW TABLES FROM match_'+text)
        query.next()
        # 保存上次满足条件查询到的表单数据(列表)
        prev_table_info = []
        # 遍历整个数据库的表名
        for i in range(query.size()):
            # query.value(0) 为当前查询的表名
            # 保存当前表的记录时间(北京时间)
            current_table_record_time_list = query.value(0).split('_')
            current_table_record_time = datetime.datetime.strptime(current_table_record_time_list[2]+current_table_record_time_list[3],'%Y%m%d%H%M')
            # 如果当前表格时间小于last_load_data_time，则跳过:
            # pdb.set_trace()
            print ('当前表的记录时间：',current_table_record_time,'当前last_load_time:',last_load_data_time)
            if time.mktime(current_table_record_time.timetuple()) < last_load_data_time:
                query.next()
                continue
            # 是否已经找到满足条件的表格
            satisfy_condition = True
            # 根据表名上的时间判断是否读取该表数据
            # 目前限制在五天内的数据表
            now = datetime.datetime.now()
            time_offset = now-current_table_record_time
            # 如果当前时间比开赛时间过去了 5 天，就不再拉取该表数据
            if int(time_offset.days) > 5:
                satisfy_condition = False

            # 开始查询满足时间段的表格
            if satisfy_condition:
                table_query = QtSql.QSqlQuery()
                print('开始分析数据:',query.value(0))
                # 读取 比赛ID，主队名称，客队名称，成交量，是否正在进行
                # 主队让球盘口，主队卖盘价格1，主队卖盘1注单
                # 客队卖盘价格1，客队卖盘1注单
                table_query.exec(
                    'select event_id,host_name,guest_name,volume,if_running,handicap_name,'
                    'handicap_host_win_back_price1,handicap_host_win_back_price1_amount,'
                    'handicap_guest_win_back_price1,handicap_guest_win_back_price1_amount,start_time'
                    ' from '+query.value(0)
                )
                table_query.next()

                # 遍历单场比赛
                for k in range(table_query.size()):
                    # if_running = 1 表示比赛正在进行，这里跳过分析
                    if table_query.value(4) == 1:
                        continue
                    # 单场比赛的字典
                    prev_table_info_match = {}
                    # 给当前比赛在结果字典中分配一个记录
                    if not table_query.value(0) in match_analysis_result.keys():
                        match_analysis_result[table_query.value(0)] = {}
                        match_analysis_result[table_query.value(0)]['event_id'] = table_query.value(0)
                        match_analysis_result[table_query.value(0)]['start_time'] = table_query.value(10)
                        match_analysis_result[table_query.value(0)]['handicap_name'] = table_query.value(5)
                        match_analysis_result[table_query.value(0)]['host_name'] = table_query.value(1)
                        match_analysis_result[table_query.value(0)]['host_price_support'] = 0
                        match_analysis_result[table_query.value(0)]['host_volume_support'] = 0
                        match_analysis_result[table_query.value(0)]['host_volume_price_support'] = 0
                        match_analysis_result[table_query.value(0)]['guest_name'] = table_query.value(2)
                        match_analysis_result[table_query.value(0)]['guest_price_support'] = 0
                        match_analysis_result[table_query.value(0)]['guest_volume_support'] = 0
                        match_analysis_result[table_query.value(0)]['guest_volume_price_support'] = 0
                    # 如果prev_table_info list存在数据
                    # 存储prev list中是否已经保存有当前比赛数据
                    prev_exit_event_id = False
                    if len(prev_table_info)>0:
                        # 遍历保存的上一个表信息
                        for prev_match_info in prev_table_info:
                            # 可能price会变成0 ，那就跳过这场比赛
                            if table_query.value(6)==0 or table_query.value(8) == 0:
                                continue
                            # 如果比赛ID相同说明是同一场比赛
                            if prev_match_info['event_id'] == table_query.value(0):
                                # 说明prev list中已经存在当前比赛数据，之后只有更新其中的value即可
                                prev_exit_event_id = True
                                # 记录时间差 以second为单位
                                table_record_time_offset = (current_table_record_time - prev_match_info['table_record_time']).seconds
                                # 投注量变化
                                volume_change = table_query.value(3)-prev_match_info['volume']
                                # 分别处理两表handicap_name , 并记录两者盘口是否相等
                                if prev_match_info['handicap_name'] == table_query.value(5):
                                    identical_handicap = True
                                    # 盘口相等可以进行水位比较
                                    handicap_host_price_change = table_query.value(6) - prev_match_info['handicap_host_win_back_price1']
                                    handicap_guest_price_change = table_query.value(8) - prev_match_info['handicap_guest_win_back_price1']
                                    # price有可能会出现0 等等异常值，要做一下特殊判断
                                    if abs(handicap_host_price_change)>1:
                                        handicap_host_price_change = 0
                                    elif abs(handicap_guest_price_change)>1:
                                        handicap_guest_price_change = 0
                                else:
                                    identical_handicap = False
                                    # 根据字符串盘口返回float型，方便比较
                                    prev_handicap_value = handicap2float(prev_match_info['handicap_name'])
                                    current_handicap_value = handicap2float(table_query.value(5))
                                    # 记录最新盘口变化
                                    handicap_change = current_handicap_value - prev_handicap_value

                                # core 判断算法
                                # 成交量增加量占之前比例，用来判断这段时间是否有大额投注
                                if prev_match_info['volume'] != 0:
                                    volume_add_ratio = volume_change / prev_match_info['volume']
                                else:
                                    volume_add_ratio = 0
                                # 暂定成》10% 为大额投注
                                volume_heavy_chip_rate = 0.10

                                # 重点水位判定，要根据赔率值所在区间有不同变化
                                host_heavy_price_change = 0.05
                                guest_heavy_price_change = 0.05
                                if table_query.value(6) >= 2:
                                    host_heavy_price_change = 0.08
                                if table_query.value(8) >= 2:
                                    guest_heavy_price_change = 0.08
                                # 限定时间差在150s内, 且满足大额投注条件
                                limit_time = 150
                                if table_record_time_offset <= limit_time:
                                    # 用盘口变化、价格变化、投注比三种方法来判断倾向
                                    # 当盘口相同
                                    if identical_handicap:
                                        # 水位变化超过限定水位
                                        if abs(handicap_host_price_change)>=host_heavy_price_change:
                                            # 根据变化方向判断倾向
                                            if handicap_host_price_change < 0:
                                                match_analysis_result[table_query.value(0)]['host_price_support'] += 1
                                                print('由于主队水位大幅下降因此 host_price_support + 1 ',table_query.value(1))
                                            else:
                                                match_analysis_result[table_query.value(0)]['host_price_support'] -= 1
                                                print('由于主队水位大幅上升因此 host_price_support - 1 ',table_query.value(2))
                                        if abs(handicap_guest_price_change) >= guest_heavy_price_change:
                                            # 根据变化方向判断倾向
                                            if handicap_guest_price_change < 0:
                                                match_analysis_result[table_query.value(0)]['guest_price_support'] += 1
                                                print('由于客队水位大幅下降因此 guest_price_support + 1 ', table_query.value(1))
                                            else:
                                                match_analysis_result[table_query.value(0)]['guest_price_support'] -= 1
                                                print('由于客队水位大幅上升因此 guest_price_support - 1 ', table_query.value(2))
                                        # 水位变化判断结束

                                        # 必须满足成交比和之前成交额达到2000
                                        if  prev_match_info['volume']>2000 and volume_add_ratio >= volume_heavy_chip_rate:
                                            if handicap_host_price_change < 0:
                                                if abs(handicap_host_price_change) < host_heavy_price_change:
                                                    match_analysis_result[table_query.value(0)]['host_volume_support'] -= 1
                                                    print('由于大量投注压向主队 host_volume_support - 1 ',table_query.value(1))
                                                else:
                                                    match_analysis_result[table_query.value(0)]['host_volume_price_support'] += 1
                                                    print('由于大额压水投注压向主队 host_volume_price_support + 1 ', table_query.value(1))
                                            if handicap_guest_price_change < 0:
                                                if abs(handicap_guest_price_change) < guest_heavy_price_change:
                                                    match_analysis_result[table_query.value(0)]['guest_volume_support'] -= 1
                                                    print('由于大量投注压向客队 guest_volume_support - 1 ', table_query.value(2))
                                                else:
                                                    match_analysis_result[table_query.value(0)]['guest_volume_price_support'] += 1
                                                    print('由于大额压水投注压向主队 guest_volume_price_support + 1 ', table_query.value(1))
                                    # else:
                                    #     # 暂时不根据盘口变化判断倾向
                                    #     print('盘口变化为：', handicap_change)
                                    #     if handicap_change > 0:
                                    #         match_analysis_result[table_query.value(0)]['host_support'] += 1
                                    #         # print('由于主队升盘因此 host_suppoer + 1')
                                    #     else:
                                    #         match_analysis_result[table_query.value(0)]['guest_support'] += 1
                                    #         # print('由于客队升盘因此 guest_suppoer + 1')

                                # 将当前数据替换prev_list 中prev table的数据
                                prev_match_info['table_record_time'] = current_table_record_time
                                prev_match_info['volume'] = table_query.value(3)
                                prev_match_info['handicap_host_win_back_price1'] = table_query.value(6)
                                prev_match_info['handicap_host_win_back_price1_amount'] = table_query.value(7)
                                prev_match_info['handicap_guest_win_back_price1'] = table_query.value(8)
                                prev_match_info['handicap_guest_win_back_price1_amount'] = table_query.value(9)
                                break
                    if not prev_exit_event_id:
                        # 将当前查询到的数据保存到prev_table_info 方便下次分析
                        prev_table_info_match['event_id'] = table_query.value(0)
                        prev_table_info_match['table_record_time'] = current_table_record_time
                        prev_table_info_match['host_name'] = table_query.value(1)
                        prev_table_info_match['guest_name'] = table_query.value(2)
                        prev_table_info_match['volume'] = table_query.value(3)
                        prev_table_info_match['if_running'] = table_query.value(4)
                        prev_table_info_match['handicap_name'] = table_query.value(5)
                        prev_table_info_match['handicap_host_win_back_price1'] = table_query.value(6)
                        prev_table_info_match['handicap_host_win_back_price1_amount'] = table_query.value(7)
                        prev_table_info_match['handicap_guest_win_back_price1'] = table_query.value(8)
                        prev_table_info_match['handicap_guest_win_back_price1_amount'] = table_query.value(9)
                        prev_table_info.append(prev_table_info_match)

                    table_query.next()
            # 记录下最后拉取表的时间
            # 先转化为时间戳再比较
            # pdb.set_trace()
            ans_time = time.mktime(current_table_record_time.timetuple())
            print('当前数据表的记录时间2：', current_table_record_time, '当前last_load_time:', last_load_data_time)
            if last_load_data_time == 0 or last_load_data_time < ans_time:
                last_load_data_time = ans_time
            query.next()
        # 查询结束
        db.close()
        print('断开查询数据库')

        # 连接记录分析数据库
        reord_db = QtSql.QSqlDatabase().addDatabase("QMYSQL")
        reord_db.setDatabaseName("match_" + text + "_analysis")
        reord_db.setHostName("127.0.0.1")  # set address
        reord_db.setUserName("root");  # set user name
        reord_db.setPassword("");  # set user pwd
        # 打开数据库
        if not reord_db.open():
            # 打开失败
            return reord_db.lastError()
        print("连接至 match_", text, "_analysis success!")
        for key in match_analysis_result:
            # 获取之前保存的数据信息
            saved_info_query = QtSql.QSqlQuery()
            # 查询出相应的比赛
            saved_info_query.exec("SELECT * FROM analysis_result WHERE event_id="+match_analysis_result[key]['event_id'])
            # 如果有当前比赛就直接更新数据
            if saved_info_query.size() > 0:
                saved_info_query.next()
                recent_saved_info_query = QtSql.QSqlQuery()
                host_price_net_support = saved_info_query.value(5)+match_analysis_result[key]["host_price_support"]-match_analysis_result[key]["guest_price_support"]
                host_volume_net_support = saved_info_query.value(6)+match_analysis_result[key]["host_volume_support"]-match_analysis_result[key]["guest_volume_support"]
                host_volume_price_net_support = saved_info_query.value(7)+match_analysis_result[key]["host_volume_price_support"]-match_analysis_result[key]["guest_volume_price_support"]
                last_updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_load_data_time))
                recent_saved_info_query.exec("UPDATE analysis_result SET host_price_net_support = "+str(host_price_net_support)+", host_volume_net_support = "+str(host_volume_net_support)+", host_volume_price_support = "+str(host_volume_price_net_support)+", last_updatetime = '%s' WHERE event_id='%s'" % (last_updatetime,match_analysis_result[key]['event_id']))
                # recent_saved_info_query.exec("UPDATE analysis_result SET host_price_net_support = "+str(host_price_net_support)+", host_volume_net_support = "+str(host_volume_net_support)+", last_updatetime = "+last_updatetime+" WHERE event_id="+match_analysis_result[key]['event_id'])
                print('update 数据库成功')
            # 如果没有当前比赛就插入数据
            else:
                insert_table = (
                    "INSERT INTO analysis_result VALUES"
                    "('%s','%s','%s','%s','%s',%d,%d,%d,%d,%d,'%s')"
                )
                recent_saved_info_query = QtSql.QSqlQuery()
                recent_saved_info_query.exec(
                    insert_table %
                    (match_analysis_result[key]['event_id'],
                    match_analysis_result[key]['host_name'],
                    match_analysis_result[key]['guest_name'],
                    match_analysis_result[key]['handicap_name'],
                    match_analysis_result[key]['start_time'],
                    match_analysis_result[key]['host_price_support']-match_analysis_result[key]['guest_price_support'],
                    match_analysis_result[key]['host_volume_support']-match_analysis_result[key]['guest_volume_support'],
                    match_analysis_result[key]['host_volume_price_support']-match_analysis_result[key]['guest_volume_price_support'],
                    0,
                    9,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_load_data_time)))
                )
                print('insert 数据库成功')
            if not reord_db.commit():
                reord_db.rollback()
        # 获取保存的数据信息
        get_saved_info_query = QtSql.QSqlQuery()
        get_saved_info_query.exec("SELECT * FROM analysis_result")
        get_saved_info_query.next()

        print('开始打印分析结果：')
        # 先清空所有表项
        self.tableWidget.clearContents()
        # 设置行数
        self.tableWidget.setRowCount(get_saved_info_query.size())
        row_count = 0
        for i in range(get_saved_info_query.size()):
            # 循环填入数据
            col_count = 0
            for j in range(self.tableWidget.columnCount()):
                if col_count == 0:
                    cnt = '%s' % (
                        utc2local(datetime.datetime.strptime(get_saved_info_query.value(4),'%Y-%m-%dT%H:%M:%SZ')).strftime('%Y-%m-%d %H:%M')
                    )
                elif col_count == 1:
                    cnt = '%s' % (
                        get_saved_info_query.value(1)
                    )
                elif col_count == 2:
                    cnt = '%s' % (
                        get_saved_info_query.value(3)
                    )
                elif col_count == 3:
                    cnt = '%s' % (
                        get_saved_info_query.value(2)
                    )
                elif col_count == 4:
                    cnt = '%d' % (
                        get_saved_info_query.value(5)
                    )
                elif col_count == 5:
                    cnt = '%d' % (
                        get_saved_info_query.value(6)
                    )
                elif col_count == 6:
                    cnt = '%d' % (
                        get_saved_info_query.value(7)
                    )
                elif col_count == 7:
                    cnt = '%s' % (
                        get_saved_info_query.value(10)
                    )
                newItem = QtWidgets.QTableWidgetItem(cnt)
                self.tableWidget.setItem(row_count, col_count, newItem)
                col_count += 1
            get_saved_info_query.next()
            row_count += 1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSortingEnabled(True)
        reord_db.close()
        print('断开记录分析数据库')
        # 断开记录分析数据库

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
