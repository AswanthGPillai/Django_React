from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from server.models import *


# district

   

@csrf_exempt
def district(request):
    districtData = list(tbl_district.objects.values())
    if request.method == 'POST':
        data = json.loads(request.body)
        district_name = data['districtName']
        tbl_district.objects.create(
            district_name = district_name
        )
        districtData = list(tbl_district.objects.values())

        return JsonResponse({"msg":"District Inserted Successfully",'district_data':districtData})
    else:
        return JsonResponse({"district_data": districtData})

    

@csrf_exempt
def district_del(request,did):
    if request.method == 'DELETE':
        tbl_district.objects.get(id=did).delete()
        return JsonResponse({"msg":"district deleted successfully"})



@csrf_exempt
def district_edit(request,uid):
    districtData = tbl_district.objects.get(id=uid)
    if request.method == 'PUT':
        data = json.loads(request.body)
        district_name = data['name']
        districtData.district_name = district_name
        districtData.save()
        return JsonResponse({"msg":"district updated successfully"})





# admin

@csrf_exempt
def admin_registration(request):
    adminData = list(tbl_admin.objects.values())
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        tbl_admin.objects.create(
            admin_name = name,
            admin_email = email,
            admin_password = password
        )
        return JsonResponse({"msg":"admin inserted successfully"})
    return JsonResponse({"adminData":adminData})


@csrf_exempt
def admin_delete(request,did):
    if request.method == 'DELETE':
        tbl_admin.objects.get(id=did).delete()
        return JsonResponse({"msg":"Data Deleted Successfully"})

@csrf_exempt
def admin_edit(request,eid):
    adminData = tbl_admin.objects.get(id=eid)
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        adminData.admin_name = name
        adminData.admin_email = email
        adminData.save()
        return JsonResponse({"msg":"admin updated successfully"})





# place

@csrf_exempt
def place(request):
    placeData = list(tbl_place.objects.values(
            "id",
            "place_name",
            "district_id",
            "district__district_name"
            ))
    if request.method == 'POST':
        place = request.POST.get("place")
        district = tbl_district.objects.get(id=request.POST.get('district'))
        tbl_place.objects.create(
            place_name = place,
            district = district
        )
        return JsonResponse({"msg":"Place created successfully"})
    return JsonResponse({"placeData":placeData})





@csrf_exempt
def place_delete(request,did):
    if request.method == 'DELETE':
        tbl_place.objects.get(id=did).delete()
        return JsonResponse({"msg":"Place Deleted Successfully"})



@csrf_exempt
def place_edit(request,eid):
    placeData = tbl_place.objects.get(id=eid)
    if request.method == 'PUT':
        data = json.loads(request.body) 
        name = data["place_name"]
        district = tbl_district.objects.get(id=data["district"])
        placeData.place_name = name
        placeData.district = district
        placeData.save()
        return JsonResponse({"msg":"place updated successfully"})


def place_filter(request,did):
    if request.method == "GET":
        placedata = tbl_place.objects.filter(district=did).values('id','place_name','district_id','district__district_name')
        return JsonResponse({"placeData":list(placedata)})



# user


@csrf_exempt
def user(request):
    if request.method == 'POST' :
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("password")
        place = tbl_place.objects.get(id=request.POST.get('place'))
        photo = request.FILES.get("photo")
        tbl_user.objects.create(
            user_name=name,
            user_email=email,
            user_address=address,
            user_password=password,
            place = place,
            user_photo=photo
            )
        return JsonResponse({'msg':"Profile Uploded.."})



def user_list(request):
    if request.method == "GET" :
        userdata = list(tbl_user.objects.values('id','user_name','user_email','user_address','user_password','user_photo','place','place__place_name','place__district__district_name'))
        return JsonResponse({'userdata':userdata})


