from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import initiatives_service

def index(request):
    initiatives = initiatives_service.get_active_initiatives()
    context = {'initiatives': initiatives}
    return render(request, 'initiatives/index.html', context)
