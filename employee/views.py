from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Employee,Department 
from django.db.models import Q

class ListEmployees(APIView):

    def get(self, request, format=None):    
    
        json_list = []
        dept = request.query_params.get("dept_name",None)
        emp_name = request.query_params.get("emp_name",None)
        min_salary = request.query_params.get("min_salary",None)
        max_salary = request.query_params.get("max_salary",None)

        if dept:
            emp_query_list = Employee.objects.filter(dept_name__dept_name=dept)
        elif emp_name:
            emp_query_list = Employee.objects.filter(emp_name=emp_name)
        elif min_salary:
            emp_query_list = Employee.objects.filter(Q(emp_salary__lt =(int(max_salary))) & Q(emp_salary__gte = (int(min_salary))) & Q(dept_name__dept_name=dept))
        else:
            emp_query_list = Employee.objects.all()

        for emp in emp_query_list:
            data = {
                "id":emp.id,
                "name" : emp.emp_name,
                "email" : emp.emp_email,
                "salary" : emp.emp_salary,
                "dept_name" : emp.dept_name.dept_name
            }
            json_list.append(data)
        
        return Response(json_list)

    def post(self, request, format=None):

        data = request.data
        deptname = Department.objects.create(dept_name = data['dept_name'])
        Employee.objects.create(emp_name = data['emp_name'], emp_email = data['emp_email'], emp_salary = data['emp_salary'], dept_name = deptname)
        
        return Response({"message":"success"})
    
    def put(self, request, format=None):

        data = request.data
        Employee.objects.filter(emp_name=data['emp_name']).update(emp_email = data['emp_email'], emp_salary = data['emp_salary'])
        
        return Response({"message":"success"})
