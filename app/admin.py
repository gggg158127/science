from django.contrib import admin
from .models import Treatment
# Register your models here.
admin.site.site_header= '方士谏'
admin.site.site_title= '方士谏'
admin.site.index_title= '方士谏'


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
 list_display = ('id', 'range','type', 'excerpt', 'bzimage',  'recommend','prescription','take','medicine','acupoint','source', )
# 文章列表里显示想要显示的字段
 list_per_page = 10

 # 后台数据列表排序方式

 list_display_links = ('id', 'type')
# 设置哪些字段可以点击进入编辑界面


