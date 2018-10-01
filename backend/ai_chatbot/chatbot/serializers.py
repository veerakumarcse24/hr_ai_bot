from rest_framework import serializers
from datetime import datetime
from chatbot.models import (
    Publisher, Author, Book)

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'

# class UsersSerializer(serializers.ModelSerializer):
#     dob = serializers.DateField(format="%d-%m-%Y")

#     class Meta:
#         model = Users
#         fields = ('employeeId', 'first_name', 'email',
#                   'login_token', 'dob', 'gaurdian_dob', 'profilepic')


# class ProfileSerializer(serializers.ModelSerializer):
#     dob = serializers.DateField(format="%d-%m-%Y")
#     gaurdian_dob = serializers.DateField(format="%d-%m-%Y")
#     # state = StateSerializer(source='State')

#     class Meta:
#         model = Users
#         # fields=('employeeId','first_name','gender','dob','contact_no','address','permanent_address','maritual_status','blood_group','profilepic','state')
#         fields = '__all__'


# class JobdetailSerializer(serializers.ModelSerializer):
#     # joining_date = serializers.DateField(format="%d-%m-%Y")

#     class Meta:
#         model = Jobdetails
#         # fields=('e_id','emp_name','branch','access_card','usertype','emp_amenities','department','designation','reporting_no','assigned_practise','joining_date','official_email','personal_email','pt_id','worksnaps_id','skype_id','pan_no','pf_no','esi_no','insurance_no','bank_acc_no','bank_name','join_salery','current_salery','emp_category','salary_category')
#         fields = '__all__'
