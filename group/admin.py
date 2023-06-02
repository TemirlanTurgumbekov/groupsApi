from django.contrib import admin
from group.models import Teacher, Student, Group


admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)



@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_of_students', 'list_of_students')

    def count_of_students(self, obj):
        return len(obj.students.all())

    def list_of_students(self, obj):
        ls = [x for x in obj.students.all()]
        return ls


@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('name_last_name', 'contacts', 'age', 'groups_list')

    def name_last_name(self, obj):
        return obj

    def groups_list(self, obj):
        return [x for x in obj.groups.all()]
