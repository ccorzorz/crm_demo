from django.db import models

# Create your models here.


class Permission(models.Model):
    caption = models.CharField(max_length=32)
    parent_id = models.ForeignKey('Permission', related_name='k', to_field='id', null=True, blank=True)
    code = models.CharField(max_length=64, null=True,blank=True)
    method = models.CharField(max_length=16, null=True,blank=True)
    kwargs = models.CharField(max_length=128, null=True,blank=True)
    is_menu = models.BooleanField(default=False)

    def __str__(self):
        return self.caption

class Role(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class RoleToPermission(models.Model):
    menu_id = models.ForeignKey(Permission, to_field='id')
    role_id = models.ForeignKey(Role, to_field='id')

    def __str__(self):
        return "%s-%s" %(self.menu_id.caption, self.role_id.name)
# 目标，根据角色列表获取权限 li
# 获取当前用户的所有标题权限
# RoleToPermission.objects.filter(role_id__in=li,menu_id__is_menu=True).\
#     values('menu_id__caption','menu_id__parent_id','menu_id__parent_id','menu_id__code')

# 获取当前用户的所有权限
# RoleToPermission.objects.filter(role_id__in=li).\
#     values('menu_id__caption','menu_id__parent_id','menu_id__parent_id','menu_id__code')

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username


class UserInfoToRole(models.Model):
    user_id = models.ForeignKey(UserInfo, to_field='id')
    role_id = models.ForeignKey(Role, to_field='id')
    def __str__(self):
        return '%s-%s' %(self.user_id.username, self.role_id.name)

# userinfo: id = 3 username=alex
# result_list = UserInfoToRole.objects.filter(user_id_id=3).values('role_id_id')
# UserInfoToRole.objects.filter(user_id_id=1).values_list('role_id_id')
# [{'role_id_id': 1}.{'role_id_id': 2}.{'role_id_id': 3}]
# 当前用户的角色列表
# li = list(map(lambda x: x['role_id_id'], result_list))
# [1,2,3]
# [(1,)]
# [1,2,3]