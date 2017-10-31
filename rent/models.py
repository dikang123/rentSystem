
from django.db import models

"""

房东类
房东昵称 房东名字 房东身份证号 房东联系方式 房东账号 房东密码 创建时间 更新时间

"""


class Landlord(models.Model):
    llord_nickname = models.CharField("房东昵称",max_length=10)
    llord_name = models.CharField("房东真实姓名",max_length=5)
    llord_ID = models.CharField("房东身份证",max_length=20)
    llord_tel = models.CharField("联系方式",max_length=15)
    llord_uid = models.IntegerField("房东账号",unique=True)
    llord_password = models.CharField("房东密码",max_length=64, unique=True)
    llord_create = models.DateTimeField("房东信息创建时间",auto_now_add=True)
    llord_update = models.DateTimeField("房东信息更新时间",auto_now=True)

    def __str__(self):
        return self.llord_name


"""
	租房需求类
	出租房屋名称 地址 范围  租金  面积 租住人数 楼层  租房创建时间  更新时间
"""


class Rentneed(models.Model):
    rent_name = models.CharField("出租房屋名称",max_length=128)
    rent_addr = models.CharField("出租地址",max_length=50)
    scope = models.IntegerField("范围")
    rental = models.IntegerField("租金")
    area = models.IntegerField("面积")
    number = models.IntegerField("租住人数")
    story = models.IntegerField("楼层")
    rent_type = models.CharField("房屋类型",max_length=20)
    rent_create = models.DateTimeField("租房信息创建时间",auto_now_add=True)
    rent_update = models.DateTimeField("租房信息更新时间",auto_now=True)
    def __str__(self):
        return self.rent_name


"""
房屋类
地址 小区名字 房屋类型 租住人数 联系电话 房东 是否出租 创建时间 更新时间 描述文字
"""


class House(models.Model):
    house_name = models.CharField("房屋名称",max_length=128,blank=False)
    address = models.CharField("地址",max_length=50)
    community_name = models.CharField("小区名字",max_length=100)
    house_type = models.CharField("房屋类型",max_length=20)
    house_number = models.IntegerField("租住人数")
    house_tel = models.CharField("联系方式",max_length=15)
    llord = models.ForeignKey("Landlord",blank=False)
    is_rent = models.BooleanField("是否出租")
    house_create = models.DateTimeField("房屋信息创建时间",auto_now_add=True)
    house_update = models.DateTimeField("房屋信息更新时间",auto_now=True)
    desc = models.TextField("房屋信息描述",default="空")

    def __str__(self):
        return self.house_name


"""

用户类
名字 昵称 用户身份证 生日 性别 联系方式 创建时间 更新时间

"""


class User(models.Model):
    username = models.CharField("真实姓名",max_length=20)
    nickname = models.CharField("昵称",max_length=20)
    userid = models.CharField("身份证",max_length=15)
    birth = models.DateTimeField("出生日期")
    sex = models.CharField("性别",max_length=5)
    tel = models.CharField("联系方式",max_length=15)
    uid = models.IntegerField("账号",unique=True)
    user_create = models.DateTimeField("用户信息创建时间",auto_now_add=True)
    user_update = models.DateTimeField("用户信息更新时间",auto_now=True)
    def __str__(self):
        return self.nickname
