from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from request_app.models import Client, FeatureRequest

# View of Index Page
def index(request):
    return render(request, 'index.html')

# To view Feature Requests
def view_requests(request):
    requests = FeatureRequest.objects.all()

    return render(request, 'view_requests.html', locals())


class FeatureRequestForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    title = forms.CharField(label="Title", max_length=200)
    client = forms.ModelChoiceField(label="Client", queryset=Client.objects.all())
    priority = forms.IntegerField(label="Priority")
    product_area = forms.ChoiceField(label="Product Areas", choices=FeatureRequest.PRODUCT_CHOICES)
    target_date = forms.DateField(label="Target Date", input_formats=["%Y-%m-%d"])
    tix_url = forms.CharField(label="Ticket URL", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)


# To submit a Feature Request
def submit_request(request, feature):
    if request.POST:
        form = FeatureRequestForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            client = form.cleaned_data['client']
            priority = form.cleaned_data['priority']
            product_area = form.cleaned_data['product_area']
            target_date = form.cleaned_data['target_date']
            tix_url = form.cleaned_data['tix_url']
            description = form.cleaned_data['description']

            if feature:
                id = form.cleaned_data['id']

                new_request = FeatureRequest(id=id, title=title, client=client, product_area=product_area,
                    priority=priority, target_date=target_date, tix_url=tix_url, description=description)

            else:
                new_request = FeatureRequest(title=title, client=client, product_area=product_area,
                    priority=priority, target_date=target_date, tix_url=tix_url, description=description)

            new_request.save()

            return HttpResponseRedirect('/view_requests')
        else:
            return render(request, 'submit_request.html', {'form': form})
    else:
        if feature:
            original = FeatureRequest.objects.get(id=feature)

            data = {
                'title': original.title,
                'client': original.client,
                'priority': original.priority,
                'product_area': original.product_area,
                'target_date': original.target_date,
                'tix_url': original.tix_url,
                'description': original.description,
                'id': original.id
            }

            form = FeatureRequestForm(data)

        else:
            form = FeatureRequestForm()

        return render(request, 'submit_request.html', {'form': form})


class ClientForm(forms.Form):
    client_name = forms.CharField(label="Client Name", max_length=50)


# To add a Client
def add_client(request):
    if request.POST:
        form = ClientForm(request.POST)

        if form.is_valid():
            client_name = form.cleaned_data['client_name']

            new_request = Client(client_name=client_name)

            new_request.save()

            return HttpResponseRedirect('/')
        else:
            return render(request, 'add_client.html', {'form': form})
    else:
        form = ClientForm()

        return render(request, 'add_client.html', {'form': form})