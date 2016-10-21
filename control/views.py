from django.shortcuts import render
from upload.models import *
from django.http import HttpResponseRedirect, HttpResponse
import subprocess
import logging
# Create your views here.

#def profileView(request):
#
#	return HttpResponseRedirect('control/control_admin.html')
	
def listView(request):
	
	query_results = NormalUser.objects.all()
        if request.user.is_authenticated():	
	    #return a response to your template and add query_results to context
	    return render(request, 'control/control.html', {'query_results':query_results})
        else:
	    return HttpResponse("please login the platform ...")
	    

def listViewAdmin(request):

        query_results = NormalUser.objects.all()
        if request.user.is_authenticated():
	    if request.method == "POST":
	 	num_id = request.POST.get("id","")
		NormalUser.objects.filter(id=num_id).delete()
        #return a response to your template and add query_results to context
            return render(request, 'control/control_admin.html', {'query_results':query_results})
        else:
	    return HttpResponse("please login the platform ...")

def releaseIso(request):
	
	query_results = NormalUser.objects.all()
	if request.user.is_authenticated() and request.method == "GET":
		if 'id' in request.GET:
			isoname = NormalUser.objects.filter(id=request.GET['id']).values('version')[0]['version']
			NormalUser.objects.filter(id=request.GET['id']).update(release="true")
			logging.debug(isoname)
			#release to pxe 
			output = subprocess.check_output(['ssh','root@172.30.13.16','/usr/bin/auto_deploy_iso_to_pxe_for_toptic','http://172.30.13.143/%s'%isoname])	
            		return render(request, 'control/control_admin.html', {'query_results':query_results})

		else:
			logging.debug('please refresh page ...')	
			return HttpResponse("please refresh page ...")
	else:
		return HttpResponse("please login the platform ...")

def withdrawIso(request):
	
	query_results = NormalUser.objects.all()
	if request.user.is_authenticated() and request.method == "GET":
		if 'id' in request.GET:
			#delete from database
			#NormalUser.objects.filter(id=request.GET['id']).delete()
			#withdraw from pxe 
			isoname = NormalUser.objects.filter(id=request.GET['id']).values('version')[0]['version']
		        output = subprocess.check_output(['ssh','root@172.30.13.16','/usr/bin/auto_off_iso_from_pxe_for_toptic',isoname])
			NormalUser.objects.filter(id=request.GET['id']).update(release="false")
			logging.debug(output)

            		return render(request, 'control/control_admin.html', {'query_results':query_results})
		else: 
			logging.debug('please refresh page ...')
			return HttpResponse("please refresh page ...")
	else:
	    return HttpResponse("please login the platform ...")
