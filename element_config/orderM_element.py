from operate.base import basepage
from selenium.webdriver.common.action_chains import ActionChains
import time
class orderM(basepage):

    '''登录操作'''
    def login(self,username,password):
        self.send_username().clear()
        self.send_username().send_keys(username)
        ActionChains(self.driver).double_click(self.send_password()).perform()
        self.send_password().send_keys(password)
        self.click_submit().click()

    '''订单通知复核'''
    def click_orderM(self):
        basepage.change_leftframe(self)
        self.click_order_check().click()
        basepage.change_mainframe(self)
    '''订单提交'''
    def order_submit(self):
        self.click_submit_button().click()

    '''订单通知复核获取供应商'''
    def get_gys(self):
        return self.by_id("conCon_txtCstName")

    '''用户管理查找供应商账号'''
    def find_gys(self,gys):
        basepage.change_leftframe(self)
        self.by_link_text("用户管理").click()
        basepage.change_mainframe(self)
        self.by_id("conCon_txtSupplier").send_keys(gys)
        #点击查询按钮
        self.by_id("WebTool_btnQuery").click()

    '''注销'''
    def Click_Cancellation(self):
        basepage.change_topframe(self)
        basepage.Cancellation(self).click()

    '''更改用户密码为abc123'''
    def Change_UserPassword(self,password):
        basepage.Click_user_edit(self).click()
        self.by_id('conCon_cbIsPassword').click()
        self.by_id('conCon_txtPassword').send_keys(password)
        self.by_id('conCon_btnDo').click()

    '''获取当前角色文本值'''
    def get_role(self):
        basepage.change_topframe(self)
        return basepage.role(self).text

    '''点击订单接收确认'''
    def click_order_confiram(self):
        return basepage.order_confiram(self).click()

    '''点击确认按钮'''
    def click_order_Accept(self):
        return basepage.click_order_confiram(self).click()

    '''进入配送单提交页面'''
    def click_Distribution_submit(self):
        return basepage.enter_Distribution_submit(self).click()

    '''新建配送单'''
    def new_bulid_Distribution(self):
       return self.by_id("WebTool_btAdd").click()

    '''填写批号，生产日期，有效期-保存'''
    def Distribution_date(self,ProDate,EendDte):
        self.by_id("conCon_gridList_txtProDate_0").click()
        self.by_id("conCon_gridList_txtProDate_0").send_keys(ProDate)
        self.by_id("conCon_gridList_txtEndDate_0").send_keys(EendDte)
        self.by_id("WebTool_btSave").click()

    '''配送单提交'''
    def submit_Distribution(self):
        self.by_id("WebTool_btTj").click()

