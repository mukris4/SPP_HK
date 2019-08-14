import time
class basepage:

    '''基础page层 封装一些常用的方法'''

    def __init__(self,driver):
        self.driver=driver
    def by_id(self,id):
        return self.driver.find_element_by_id(id)
    def by_name(self,name):
        return self.driver.find_element_by_name(name)
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)
    def by_tag_name(self,tag_name):
        return self.driver.find_element_by_tag_name(tag_name)
    def by_link_text(self,link_text):
        return self.driver.find_element_by_link_text(link_text)
    def by_tag_className(self, className):
        return self.driver.find_element_by_class_name(className)
    def dig_alert(self,assert_text,msg=None):
        #弹窗处理
        dig_alert = self.driver.switch_to.alert
        self.assertIn(assert_text, dig_alert.text,msg)
        dig_alert.accept()

    def change_leftframe(self):
        # 切换至leftframe
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
    def change_mainframe(self):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')
    def change_topframe(self):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('topFrame')
    '''mianframe 标题'''
    def get_title(self):
        return self.by_tag_className("titlebt").text

    '''登录'''
    # 定位账号输入框
    def send_username(self):
        return self.by_id("username")
    # 定位密码输入框
    def send_password(self):
        return self.by_id("password")
    # 定位登录按钮
    def click_submit(self):
        return self.by_id("ImageBtLogin")

    '''订单通知复核元素'''
    def click_order_check(self):
        return self.by_link_text("订单通知复核")
    def click_submit_button(self):
        return self.by_id("WebTool_btTj")
    '''注销'''
    def Cancellation(self):
        return self.by_link_text("注销")
    '''用户管理-编辑'''
    def Click_user_edit(self):
        return  self.by_xpath('//*[@id="conCon_gridList"]/tbody/tr[2]/td[2]/a')
    '''当前角色'''
    def role(self):
        return self.by_id("userName1")
    '''订单接收确认'''
    def order_confiram(self):
        return self.by_link_text("订单接收确认")
    '''定位确认按钮'''
    def click_order_confiram(self):
        return  self.by_id("WebTool_btSave")
    '''进入配送单提交页面'''
    def enter_Distribution_submit(self):
        return self.by_link_text("配送单提交")
