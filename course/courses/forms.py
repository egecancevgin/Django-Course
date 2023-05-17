from django import forms
from courses.models import Course
from django.forms import widgets
from django.forms import TextInput, Textarea

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Course Title", 
#         required=True,
#         error_messages={
#             "required":"You should enter a course title."
#         },
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            "title": "Course Title",
            "description": "Course Description"
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required": "You must enter a course title.",
                "max_length": "You can enter up to 50 characters."
            },
            "description": {
                "required": "You must enter a course description."
            }
        }