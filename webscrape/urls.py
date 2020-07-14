from django.urls import path
from webscrape import views
'''
urlpatterns = [
    path('api/tutorials',views.tutorial_list),
    path('api/tutorials/<int:pk>', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published),

]'''

urlpatterns = [
    path('scraping',views.start_scrape),
    path('property', views.property_list),
    path('property/<int:pk>', views.property_detail),
    ]

