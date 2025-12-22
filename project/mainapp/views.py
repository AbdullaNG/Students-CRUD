from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .forms import StudentForm
from .models import Student


def home(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = StudentForm()
	
	students = Student.objects.all()
	return render(request, 'mainapp/index.html', {'form': form, 'students': students})


def student_detail(request, pk):
	student = Student.objects.all().get(pk=pk)
	return render(request, 'mainapp/detail.html', {'student': student})


class StudentUpdate(UpdateView):
	model = Student
	fields = '__all__'
	template_name = 'mainapp/update.html'
	success_url = reverse_lazy('update')

	def get_success_url(self):
		return reverse_lazy('home')


class StudentDelete(DeleteView):
	model = Student
	success_url = reverse_lazy('home')
