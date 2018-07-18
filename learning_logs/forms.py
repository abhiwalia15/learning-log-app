from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

def edit_entry(request, entry_id):
	'''edit an existing entry'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	if request.method != 'POST':
		#initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
		
	else:
		#POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
			
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)
			

