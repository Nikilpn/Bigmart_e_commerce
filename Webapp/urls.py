from django.urls import path
from Webapp import views


urlpatterns=[
    path('',views.homepage,name="home"),
    path('About/', views.aboutpage, name="About"),
    path('Contact/', views.contactpage, name="Contact"),
    path('products/', views.products, name="products"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('filtered_products/<cat_name>/', views.filtered_products, name="filtered_products"),

    path('single_product/<int:pro_id>/', views.single_product, name="single_product"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('save_registration_page/', views.save_registration_page, name="save_registration_page"),
#signin with the help of data saved in registerdatabase
    path('User_login/', views.User_login, name="User_login"),

    path('user_logout/', views.user_logout, name="user_logout"),

    path('save_cart/', views.save_cart, name="save_cart"),

    path('cart_page/', views.cart_page, name="cart_page"),

    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),

    path('user_login_page/', views.user_login_page, name="user_login_page"),

    path('checkout_page/', views.checkout_page, name="checkout_page"),

    path('save_billingaddress/', views.save_billingaddress, name="save_billingaddress"),

#####payement---page-------------------

    path('paymentpage/', views.paymentpage, name="paymentpage"),


]