from django.contrib import admin
from .models import *


class STUDENT_Admin(admin.ModelAdmin):
	list_display = [
		'STUDENTID',
		'NAME_STU',
		'PASSWD',
		'SEX',
		'ID_CLA',
		'ID_DEP',
		'BIRTHDAY',
		'NATIVE_PLACE'
	]
	search_fields = [('STUDENTID'), ]


class CHANGE_Admin(admin.ModelAdmin):
	list_display = [
		'ID_CHA',
		'STUDENTID',
		'CHANGE',
		'REC_TIME',
		'DESCRIPTION'
	]
	search_fields = [('STUDENTID'),('CHA_ID'),]


class REWARD_Admin(admin.ModelAdmin):
	list_display = [
		'ID_REW',
		'STUDENTID',
		'LEVELS',
		'REC_TIME',
		'DESCRIPTION'
		]
	search_fields = [('STUDENTID'), ('ID_REW')]


class PUNISHMENT_Admin(admin.ModelAdmin):
	list_display = [
		'ID_PUN',
		'STUDENTID',
		'LEVELS',
		'REC_TIME',
		'ENABLE',
		'DESCRIPTION'
	]
	search_fields = [('STUDENTID'), ('ID_PUN')]


class DEPARTMENT_Admin(admin.ModelAdmin):
	list_display = [
		'ID_DEP',
		'NAME_DEP'
	]
	search_fields = [('ID_DEP')]


class CLASS_Admin(admin.ModelAdmin):
	list_display = [
		'ID_CLA',
		'NAME_CLA',
		'NAME_DEP',
	]
	search_fields = [('ID_CLA')]


class CHANGE_CODE_Admin(admin.ModelAdmin):
	list_display = [
		'CODE',
		'DESCRIPTION'
	]
	search_fields = [('CODE')]


class REWARD_CODE_Admin(admin.ModelAdmin):
	list_display = [
		'CODE',
		'DESCRIPTION'
	]
	search_fields = [('CODE')]


class PUNISH_CODE_Admin(admin.ModelAdmin):
	list_display = [
		'CODE',
		'DESCRIPTION'
	]
	search_fields = [('CODE')]

admin.site.register(STUDENT, STUDENT_Admin)
admin.site.register(CHANGE, CHANGE_Admin)
admin.site.register(REWARD, REWARD_Admin)
admin.site.register(PUNISHMENT, PUNISHMENT_Admin)
admin.site.register(DEPARTMENT, DEPARTMENT_Admin)
admin.site.register(CLASS, CLASS_Admin)
# admin.site.register(CHANGE_CODE, CHANGE_CODE_Admin)
# admin.site.register(REWARD_CODE, REWARD_CODE_Admin)
# admin.site.register(PUNISH_CODE, PUNISH_CODE_Admin)
admin.AdminSite.site_header = "管理后台"
admin.AdminSite.site_title = "管理"
# Register your models here.
