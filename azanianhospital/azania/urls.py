from django.urls import path
from .views import AddUser, DeleteUser, AddAppointment, DeleteAppointment


urlpatterns = [
    path("add_user/", AddUser.as_view(), name ="user_add"),
    path("delete_user/<int:pk>/", DeleteUser.as_view(), name ="user_delete"),
    path("create_appointment/", AddAppointment.as_view(), name="create_appmnt"),
    path("delete_appointment/<int:pk>/", DeleteAppointment.as_view(), name="delete_appmnt")

]
