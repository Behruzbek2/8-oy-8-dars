from rest_framework import serializers
from .models import Teacher, Class, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']

class ClassSerializer(serializers.ModelSerializer):
    students = StudentMiniSerializer(many=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'students']

    def create(self, validated_data):
        students_data = validated_data.pop('students')
        class_instance = Class.objects.create(**validated_data)
        for student in students_data:
            Student.objects.create(student_class=class_instance, **student)
        return class_instance

    def update(self, instance, validated_data):
        students_data = validated_data.pop('students', None)
        instance.name = validated_data.get('name', instance.name)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.save()

        if students_data:
            instance.students.all().delete()
            for student in students_data:
                Student.objects.create(student_class=instance, **student)

        return instance

class StudentSerializer(serializers.ModelSerializer):
    class_name = serializers.RelatedField(source='student_class', read_only=True)
    class_str = serializers.StringRelatedField(source='student_class')
    class_pk = serializers.PrimaryKeyRelatedField(source='student_class', read_only=True)
    class_link = serializers.HyperlinkedRelatedField(
        source='student_class',
        read_only=True,
        view_name='class-detail'
    )
    class_slug = serializers.SlugRelatedField(
        source='student_class',
        read_only=True,
        slug_field='name'
    )
    url = serializers.HyperlinkedIdentityField(view_name='student-detail')

    class Meta:
        model = Student
        fields = ['id', 'name', 'url', 'class_name', 'class_str', 'class_pk', 'class_link', 'class_slug']

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}
