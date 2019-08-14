from element_config.orderM_element import orderM
from operate import base
import time,random
import unittest
from ddt import ddt,data,unpack
from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
'''
PO模式
'''
# 登录
@ddt
class orderMangeCase(unittest.TestCase,orderM):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Ie()
        cls.driver.get('http://192.168.1.24:8041')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()

    @data(
        # ['', 'abc123','用户名不能为空'],
        ['admin', 'abc123','']
        )
    @unpack
    def test_a1_login(self,username,password,assert_text):
        """管理员登录"""
        orderM.login(self,username,password)
        if username=="admin":
            base.basepage.change_topframe(self)
            result=orderM.get_role(self)
            self.assertIn("管理员" , result)
        else:
            base.basepage.dig_alert(self,assert_text)

    def test_a2_enter_Order_notification_review(self):
        """进入订单通知复核页面"""
        orderM.click_orderM(self)
        title = base.basepage.get_title(self)
        self.assertEqual(title, "订单通知复核")

    # @unittest.skip('暂不执行')
    def test_a3_Order_notification_review(self):
        """订单通知复核提交"""
        orderM.order_submit(self)
        base.basepage.dig_alert(self,"提交成功")
    def test_a4_get_gys(self):
        '''获取供应商账号'''
        gys=orderM.get_gys(self).get_attribute('value')
        orderM.find_gys(self,gys)
        #获取用户名
        global  username
        username = self.by_xpath('//*[@id="conCon_gridList"]/tbody/tr[2]/td[6]').text
        self.assertIsNotNone(username,msg='登录名不存在')
        global realname
        realname=self.by_id('conCon_gridList_LabelTrueName_0').text

    # @unittest.skip('暂不执行')
    def test_a5_ChangePassword(self):
        '''修改用户密码'''
        orderM.Change_UserPassword(self,'abc123')
        base.basepage.dig_alert(self, "","IE浏览器当弹窗提示'不允许此页创建更多的消息'时获取不到弹窗的文本值，如果提交不成功则报错")

    def test_a6_gys_login(self):
        '''切换供应商登录'''
        orderM.Click_Cancellation(self)
        orderM.login(self, username, "abc123")

        result = orderM.get_role(self)
        self.assertIn(realname , result)

    def test_a7_Order_Acceptance_Confirmation(self):
        '''进入订单接收确认页面'''
        base.basepage.change_leftframe(self)
        orderM.click_order_confiram(self)
        base.basepage.change_mainframe(self)
        title=base.basepage.get_title(self)
        self.assertEqual(title, "订单接收确认")

    # @unittest.skip('暂不执行')
    def test_a8_Order_Accept(self):
        '''订单接收确认-点击确认按钮'''
        global OrderNo
        OrderNo=self.by_id("conCon_txtBillNo").get_attribute('value')
        orderM.click_order_Accept(self)
        base.basepage.dig_alert(self,"","IE浏览器当弹窗提示'不允许此页创建更多的消息'时获取不到弹窗的文本值，如果提交不成功则报错")

    def test_a9_Delivery_order_submission(self):
        '''进入配送单提交页面'''
        base.basepage.change_leftframe(self)
        orderM.click_Distribution_submit(self)
        base.basepage.change_mainframe(self)
        title=base.basepage.get_title(self)
        self.assertEqual(title, "配送单提交")

    def test_b1_new_build(self):
        '''新建配送单'''
        orderM.new_bulid_Distribution(self)
        # 选择仓库
        select = self.by_id("conCon_ddlCKName")
        # 获取select里面的option标签(仓库名称)
        options_list = select.find_elements_by_tag_name('option')
        # 遍历option
        Warehouse = []
        for option in options_list:
            Warehouse.append(option.get_attribute("value"))
        for selectWarehouse in Warehouse:
            Select(self.by_id("conCon_ddlCKName")).select_by_value(selectWarehouse)
            time.sleep(2)
            self.by_id("conCon_btnAddDtl").click()
            time.sleep(4)
            windows = self.driver.window_handles
            # print(windows)
            self.driver.switch_to.window(windows[1])
            #根据订单号搜索订单
            WebDriverWait(self.driver, 15, 5).until(
                EC.presence_of_element_located((By.ID, 'txtBillNo'))).send_keys(OrderNo)

            self.by_id("btQuery").click()
            billNo = self.by_xpath('//*[@id="gridLogList"]/tbody/tr[2]/td[2]').text
            if billNo == "1": #如果订单不为空
                self.by_id("gridLogList_selected_0").click()
                self.by_id("btOK").click()
                break
            else:
                self.by_id("btCance").click()
                # 判断当前窗口
                all_handles = self.driver.window_handles
                self.driver.switch_to.window(all_handles[0])
                base.basepage.change_mainframe(self)
        self.assertEqual(billNo, "1")
    def test_b2_save__Distribution(self):
        '''填写批号，生产日期，有效期-保存'''
        # 切换至原来窗口
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        base.basepage.change_mainframe(self)
        # 批号
        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'conCon_gridList_txtLotNo_0'))).send_keys(random.randint(1, 10))
        #生产日期，有效期
        orderM.Distribution_date(self,"2016-01-01","2060-10-10")
        base.basepage.dig_alert(self, "保存成功")
    def test_b3_submit_Distribution(self):
        '''配送单提交'''
        orderM.submit_Distribution(self)
        base.basepage.dig_alert(self,"","IE浏览器当弹窗提示'不允许此页创建更多的消息'时获取不到弹窗的文本值，如果提交不成功则报错")















