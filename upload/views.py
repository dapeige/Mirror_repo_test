from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from upload.models import *
import logging
# Create your views here.
# Normal user form , one field is username and the other is headImg .
class NormalUserForm(forms.Form):
	isofile = forms.FileField()
# fill in blank fields and send a 'POST' request 
def registerNormalUser(request):
    if request.user.is_authenticated():
        if request.method == "POST":
	    uf = NormalUserForm(request.POST, request.FILES)
	    if uf.is_valid():
	        version = uf.cleaned_data['isofile']
	        #get the info of the form
		if str(version).endswith(".iso") == False:
			return HttpResponse('please check the format')
		#ownername = request.POST.get('username')
                #logging.debug(ownername)
		ownername = "admin"
		isofile = uf.cleaned_data['isofile']
		state = "pre"
		release = "false"
		#write in database
		normalUser = NormalUser()
		#normalUser.username = username
		normalUser.version = version
		normalUser.ownername = ownername
		normalUser.isofile = isofile 
		normalUser.state = state
		normalUser.release = release
		normalUser.save()
		# HttpResponse('Upload Succeed!')
                return HttpResponseRedirect("/control_admin/")
	else:
		uf = NormalUserForm()
	return render(request, 'upload/register.html', {'uf':uf})
    else:
	return HttpResponse('please log in the platform')
