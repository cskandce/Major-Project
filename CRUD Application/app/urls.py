from django.urls import path,include
from .import views
urlpatterns = [
    #This path renders insert form to browser and name is used to call the form
    path("",views.InsertPageView,name="insertpage"),  
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.ShowPage,name="showpage"),
    #Because we need to fetch one particular user data
    #we want to pass id of that user
    #to pass id to view we want to take it through the pathway of url  
    path("editpage/<int:pk>",views.EditPage,name="editpage"), 
    path("update/<int:pk>",views.UpdateData,name="update"), 
    path("delete/<int:pk>",views.DeleteData,name="delete"),   
]
