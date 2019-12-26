from django.db import models


class CHANGE_CODE(models.Model):
	CODE = models.IntegerField(default=0, verbose_name="学籍变更代码")
	DESCRIPTION = models.CharField(max_length=10, verbose_name="学籍变更说明")
	def __str__(self):
		return self.DESCRIPTION

	class Meta:
		db_table = "CHANGE_CODE"
		verbose_name_plural = "学籍变更代码表"


class REWARD_CODE(models.Model):
	CODE = models.IntegerField(default=0, verbose_name="奖励级别代码")
	DESCRIPTION = models.CharField(max_length=20, verbose_name="奖励级别说明")
	
	def __str__(self):
		return self.DESCRIPTION

	
	class Meta:
		db_table = "REWARD_CODE"
		verbose_name_plural = "奖励级别代码表"


class PUNISH_CODE(models.Model):
	CODE = models.IntegerField(default=0, verbose_name="处罚级别代码")
	DESCRIPTION = models.CharField(max_length=20, verbose_name="处罚级别说明")

	def __str__(self):
		return self.DESCRIPTION


	class Meta:
		db_table = "PUNISH_CODE"
		verbose_name_plural = "处罚级别代码表"



class DEPARTMENT(models.Model):
	ID_DEP = models.IntegerField(default=1, primary_key=True, verbose_name="院系编号")
	NAME_DEP = models.CharField(max_length=20, verbose_name="全称")	

	def __str__(self):
		return str(self.NAME_DEP)


	class Meta:
		db_table = "DEPARTMENT"
		verbose_name_plural = "院系信息表" 


class STUDENT(models.Model):
	sex_choice = (('男', '男'), ('女', '女'))
	STUDENTID = models.IntegerField(default=1, verbose_name="学号", primary_key=True)
	PASSWD = models.CharField(max_length=20, default="12345",verbose_name="密码")
	NAME_STU = models.CharField(max_length=20, verbose_name="姓名")
	SEX = models.CharField(max_length=5, choices=sex_choice, verbose_name="性别")
	ID_CLA  = models.ForeignKey("CLASS", on_delete=models.CASCADE, verbose_name="班级")
	ID_DEP = models.ForeignKey("DEPARTMENT", on_delete=models.CASCADE, verbose_name="所属院系")
	BIRTHDAY = models.DateField(verbose_name="生日")
	NATIVE_PLACE = models.CharField(max_length=50, verbose_name="籍贯")

	
	def __str__(self):
		return self.NAME_STU

	class Meta:
		db_table = "STUDENT"
		verbose_name_plural = "学生个人信息表"


class CLASS(models.Model):
	ID_CLA = models.IntegerField(default=1, primary_key=True, verbose_name="班级编号")
	NAME_CLA = models.CharField(max_length=20, verbose_name="班级全称")
	NAME_DEP = models.ForeignKey('DEPARTMENT', verbose_name="所属院系", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.NAME_CLA)

	
	class Meta:
		db_table = "CLASS"
		verbose_name_plural = "班级信息表"

	
class CHANGE(models.Model):
	ID_CHA = models.IntegerField(default=0, verbose_name="记录号", primary_key=True)
	STUDENTID = models.ForeignKey("STUDENT", on_delete=models.CASCADE, verbose_name="学号")
	CHANGE = models.ForeignKey("CHANGE_CODE", on_delete=models.CASCADE, verbose_name="变更代码")
	REC_TIME = models.DateField(verbose_name="记录时间", default="")
	DESCRIPTION = models.CharField(max_length=200, verbose_name="描述")


	class Meta:
		db_table = 'CHANGE'
		verbose_name_plural = "学籍信息变更表"

class REWARD(models.Model):
	ID_REW = models.IntegerField(default=0, verbose_name="记录号", primary_key=True)
	STUDENTID = models.ForeignKey('STUDENT', on_delete=models.CASCADE, verbose_name="学号")
	LEVELS = models.ForeignKey("REWARD_CODE", verbose_name="级别代码", on_delete=models.CASCADE)
	REC_TIME = models.DateField(verbose_name="记录时间", default="")
	DESCRIPTION = models.CharField(max_length=200, verbose_name="描述")


	class Meta:
		db_table = "REWARD"
		verbose_name_plural = "奖励记录信息表"


class PUNISHMENT(models.Model):
	ID_PUN = models.IntegerField(default=0, verbose_name="记录号", primary_key=True)
	STUDENTID = models.ForeignKey("STUDENT", verbose_name="学号", on_delete=models.CASCADE)
	LEVELS = models.ForeignKey("PUNISH_CODE", verbose_name="级别代码", on_delete=models.CASCADE)
	ENABLE = models.BooleanField(verbose_name="是否生效", default=True)
	REC_TIME = models.DateField(verbose_name="记录时间", default="")
	DESCRIPTION = models.CharField(max_length=200, verbose_name="描述")


	class Meta:
		db_table = "PUNISHMENT"
		verbose_name_plural = "处罚记录信息表"
# Create your models here.
