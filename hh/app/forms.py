from datetime import date

from django import forms
from app.models import Resume, Vacancy


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('title', 'name', 'surname', 'patronymic', 'date_of_birth', 'email', 'skills', 'experience', 'education')

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth > date.today():
            raise forms.ValidationError('Date of birth cannot be in the future.')
        return date_of_birth

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or '@' not in email:
            raise forms.ValidationError('Enter a valid email address.')
        return email

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'company_name', 'salary', 'required_skills', 'responsibilities', 'address')

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary <= 0:
            raise forms.ValidationError('Salary must be a positive number.')
        return salary

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError('Address cannot be empty.')
        return address
