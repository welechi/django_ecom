from django.shortcuts import render, redirect
from oscar.core.loading import get_class, get_model
from oscar.apps.promotions.views import HomeView as CoreHomeView

Category = get_model('catalogue', 'category')


class HomeView(CoreHomeView):
    template_name = 'promotions/home.html'

    def get(self, request):
        categories = Category.objects.all()
        args = {
            'categories': categories
        }
        return render(request, self.template_name, args)  

