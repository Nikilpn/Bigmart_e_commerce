from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('category/',views.category,name="category"),

    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:edit_id>', views.edit_category, name="edit_category"),
    path('update_category/<int:up_id>', views.update_category, name="update_category"),
    path('delete_category/<int:del_id>', views.delete_category, name="delete_category"),
    path('login_page/', views.login_page, name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('products_page/', views.products_page, name="products_page"),
    path('save_product/', views.save_product, name="save_product"),
    path('product_display/', views.product_display, name="product_display"),
    path('products_edit/<int:pro_id>/', views.products_edit, name="products_edit"),
    path('update_product/<int:up_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:del_id>/', views.delete_product, name="delete_product"),

    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_details/<int:del_id>/', views.delete_details, name="delete_details"),



]